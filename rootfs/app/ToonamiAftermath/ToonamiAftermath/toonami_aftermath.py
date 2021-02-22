from datetime import date, datetime, timedelta
from dateutil import rrule, parser
import dicttoxml
import json
import logging
import os
import pathlib
import ssl
import urllib
from urllib.request import urlopen
from xmltv.models import *
from xmltv import xmltv_helpers
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.serializers.config import SerializerConfig
from ToonamiAftermath import media, mediaInfo, taChannels

_NEW_DATE_FORMAT_MINIMAL = '%Y%m%d'
_NEW_DATE_FORMAT = '%Y%m%d%H%M%S %z'
_NEW_DATE_FORMAT_NO_TZ = '%Y%m%d%H%M%S'
_EXCLUDED_STRINGS = [
    'a.k.a. Cartoon',
    'IMDbPro',
    'See full cast & crew',
    'See more'
]

class ToonamiAftermath:
    """
    Toonami Aftermath Class
    """
    channels_data_file = pathlib.Path(__file__).parent / 'data' / 'channels.xml'
    config_dir = pathlib.Path('/config')
    data_out_dir = '/data/ToonamiAftermath/'
    if os.path.exists(data_out_dir):
        m3u_file_name = data_out_dir + 'ToonamiAftermath.m3u'
        xmltv_file_name = data_out_dir + 'ToonamiAftermathGuide.xml'
        media_info_file = config_dir / 'ToonamiAftermathMediaInfo.xml'
    else:
        m3u_file_name = 'ToonamiAftermath.m3u'
        xmltv_file_name = 'ToonamiAftermathGuide.xml'
        media_info_file = 'ToonamiAftermathMediaInfo.xml'

    if os.path.exists(config_dir):
        log_file = config_dir / 'log' / 'ToonamiAftermath.log'
    else:
        log_file = 'ToonamiAftermath.log'

    GUIDE_ITEMS_PER_CHANNEL = os.getenv('GUIDE_ITEMS_PER_CHANNEL', 200)
    USE_EPISODE_CACHE = os.getenv('USE_EPISODE_CACHE', True)

    dicttoxml.LOG.setLevel(logging.ERROR)
    LOGGER = logging.getLogger('ToonamiAftermath-Logger')
    logging.basicConfig(format='%(asctime)s %(name)s %(funcName)s [%(levelname)s]: %(message)s',
                        level=logging.getLevelName(os.getenv('LOG_LEVEL', 'ERROR')),
                        handlers=[logging.FileHandler(log_file),
                                  logging.StreamHandler()])

    URL_CONTEXT = ssl._create_unverified_context()
    XML_PARSER = XmlParser(context=XmlContext())
    MEDIA_GUIDE_OBJECT = media.Root(element=[])
    SERIALIZER_CONFIG = SerializerConfig(pretty_print=True)

    CHANNELS: taChannels.Root
    all_episodes = mediaInfo.Root(element=[])
    TV_OBJECT: xmltv.Tv

    def main(self):
        self.TV_OBJECT = xmltv.Tv(
            date=str(date.today()),
            source_info_url='https://api.toonamiaftermath.com',
            source_info_name='Toonami-Aftermath',
            generator_info_url='https://api.toonamiaftermath.com',
            generator_info_name='Toonami-Aftermath'
        )
        self.CHANNELS = xmltv_helpers.serialize_xml_from_file(
            xml_file_path=pathlib.Path(self.channels_data_file),
            serialize_clazz=taChannels.Root
        )

        if self.USE_EPISODE_CACHE and os.path.exists(self.media_info_file):
            self.LOGGER.debug('Loading media info data.')
            self.all_episodes = xmltv_helpers.serialize_xml_from_file(
                xml_file_path=pathlib.Path(self.media_info_file),
                serialize_clazz=mediaInfo.Root
            )

        self.get_channels()
        for channel in self.CHANNELS.element:
            self.get_media(channel_object=channel)

        self.adapt_media_objects_to_xmltv_object()

        xmltv_helpers.write_file_from_xml(
            xml_file_path=pathlib.Path(self.xmltv_file_name),
            serialize_clazz=self.TV_OBJECT
        )
        self.write_to_m3u_file(m3u_out_file=self.m3u_file_name)

        if self.USE_EPISODE_CACHE:
            xmltv_helpers.write_file_from_xml(
                xml_file_path=pathlib.Path(self.media_info_file),
                serialize_clazz=self.all_episodes
            )

    def get_channels(self):
        """
        This method loads the channels from the data file for the project.
        """
        if not self.channels_data_file or not os.path.exists(self.channels_data_file):
            self.LOGGER.fatal('Unable to find or open {}'.format(self.channels_data_file))
            exit(1)

        for channel in self.CHANNELS.element:
            self.LOGGER.debug('Adapting channel {} to Channel object and adding it to TV_OBJECT.'.format(channel.displayName))
            self.TV_OBJECT.channel.append(
                Channel(
                    id=channel.id,
                    display_name=[DisplayName(content=[channel.displayName], lang=channel.lang)],
                    icon=[Icon(src=channel.icon)],
                    url=[channel.url]
                )
            )

    def get_media(self, channel_object: taChannels.Element):
        """
        Get the media (guide) from the given data. If no URL is specified a mock guide object will be made.
        :param channel_object: taChannel Element Object.
        :return: N/A
        """
        if channel_object.scheduleUrl is not None:
            prepared_url = channel_object.scheduleUrl + \
                           '&dateString={}'.format(date.today()) + \
                           '&count={}'.format(self.GUIDE_ITEMS_PER_CHANNEL)
            json_object = self.get_json_obj_from_url(json_url=prepared_url)
            if json_object is None:
                self.LOGGER.error('The URL {} has no media info.'.format(prepared_url))
                return

            self.LOGGER.debug('Transforming json object from {} into XML and then again into a media XML object.'.format(prepared_url))
            media_objects = self.XML_PARSER.from_bytes(
                dicttoxml.dicttoxml(
                    obj=json_object,
                    root=False,
                    attr_type=False,
                    item_func=lambda x: 'element' if x == '' else x
                ),
                media.Root
            )

            position = 0
            self.LOGGER.debug('Looping through the media object elements to add additional data and scrape the media info.')
            for media_element in media_objects.element:
                # If there's another element then add the current element's stop time.
                if position < len(media_objects.element) - 1:
                    media_element.stopDate = self.get_proper_date_time(date_time_string='{}{}'.format(str(media_objects.element[position + 1].startDate), channel_object.offset), new_format=_NEW_DATE_FORMAT)

                if media_element.name is None and media_element.blockName is not None:
                    media_element.name = media_element.blockName

                if media_element.name is not None:
                    if media_element.info is not None and media_element.info.fullname is not None:
                        episode_urlized = urllib.parse.quote(media_element.info.fullname)
                    else:
                        episode_urlized = urllib.parse.quote(media_element.name)
                    full_query_url = channel_object.episodeQueryUrl + '?name={}'.format(episode_urlized)
                    if media_element.info is not None and media_element.info.year is not None:
                        full_query_url += '&year={}'.format(media_element.info.year)
                    if media_element.episodeNumber is not None:
                        full_query_url += '&episode={}'.format(media_element.episodeNumber)
                    media_element.queryUrl = full_query_url
                    media_element.lang = channel_object.lang
                    media_element.channelUrl = channel_object.url
                    media_element.startDate = self.get_proper_date_time(date_time_string='{}{}'.format(str(media_element.startDate), channel_object.offset), new_format=_NEW_DATE_FORMAT)
                    media_element.channel = channel_object.id
                    self.get_media_info(media_info_url=full_query_url)
                self.MEDIA_GUIDE_OBJECT.element.append(media_element)
                position += 1
        else:
            _start_time = datetime.now().replace(minute=0, second=0, microsecond=0)
            _end_time = _start_time + timedelta(days=1)
            self.LOGGER.debug('The channel {} doesn\'t have a TV guide - Making a 24 hour Mock guide from {} until {}.'.format(
                channel_object.displayName, _start_time, _end_time))
            for block in rrule.rrule(rrule.HOURLY, dtstart=_start_time, until=_end_time):
                _block_start_time = self.get_proper_date_time(block, _NEW_DATE_FORMAT_NO_TZ)
                _block_end_time = self.get_proper_date_time(block + timedelta(hours=1), _NEW_DATE_FORMAT_NO_TZ)
                self.LOGGER.debug('Making 1 hour block from {} until {}.'.format(_block_start_time, _block_end_time))
                self.TV_OBJECT.programme.append(
                    Programme(
                        clumpidx=None,
                        channel=channel_object.id,
                        icon=[Icon(src=channel_object.icon)],
                        start=_block_start_time,
                        stop=_block_end_time,
                        title=[Title(content=[channel_object.displayName], lang=channel_object.lang)]
                    )
                )
                _start_time = _end_time

    def get_media_info(self, media_info_url: str):
        """
        Get the specified media elements info.
        :param media_info_url: The URL the media info is at.
        """
        found = False
        self.LOGGER.debug('Checking if the mediaInfo for {} is present in our current list before grabbing it.'.format(media_info_url))
        for element in self.all_episodes.element:
            if element.queryUrl == media_info_url:
                found = True
                break
        if not found:
            self.LOGGER.debug('mediaInfo data for {} wasn\'t found in list so we will scrape it.'.format(media_info_url))
            json_object = self.get_json_obj_from_url(json_url=media_info_url)
            if json_object is None:
                return

            self.LOGGER.debug('Transforming json object from {} into XML and then again into a mediaInfo XML object.'.format(media_info_url))
            media_info_element = self.XML_PARSER.from_bytes(
                dicttoxml.dicttoxml(
                    obj=json_object,
                    root=False,
                    attr_type=False,
                    item_func=lambda x: 'element' if x == '' else x
                ),
                mediaInfo.Element
            )
            media_info_element.queryUrl = media_info_url
            self.LOGGER.debug('Clearing out un-needed data from the media info element for: {}.'.format(media_info_element))
            media_info_element.productionCo.productionCo = [producer for producer in media_info_element.productionCo.productionCo if producer not in _EXCLUDED_STRINGS]
            media_info_element.creators.creators = [creator for creator in media_info_element.creators.creators if creator not in _EXCLUDED_STRINGS]
            self.all_episodes.element.append(media_info_element)

    def get_json_obj_from_url(self, json_url: str):
        """
        Get the json object from the specified url.
        :param json_url: The URL the json data is at.
        :return: the json object.
        """
        try:
            self.LOGGER.debug('Attempting to download the json data from the URL {}.'.format(json_url))
            raw_data = urlopen(json_url, context=self.URL_CONTEXT).read()
            if len(raw_data) == 0:
                self.LOGGER.debug('Couldn\'t scrape data from the url: {}'.format(json_url))
                return None
            else:
                self.LOGGER.debug('Successfully pulled data from the url {} so we will not reconstruct it into a python data object.'.format(json_url))
                return [json.loads(raw_data)]
        except urllib.error.URLError as connectionError:
            self.LOGGER.error('Error getting data from URL {} due to connection issue.'.format(json_url), connectionError)

    def adapt_media_objects_to_xmltv_object(self):
        """
        Adapt the media guide object to the TV object.
        :return:
        """
        self.LOGGER.debug('Going to adapt media objects into xmltv objects.')
        for media_object in self.MEDIA_GUIDE_OBJECT.element:
            media_info_object = None
            for element in self.all_episodes.element:
                if element.queryUrl == media_object.queryUrl:
                    self.LOGGER.debug('Found the corresponding mediaInfo object for the media_object with a url of {}.'.format(media_object.queryUrl))
                    media_info_object = element
                    break

            try:
                _category = None
                _credits = None
                _date = None
                _desc = None
                _episode_num = None
                _icon = None
                _rating = None
                _star_rating = None
                _sub_title = None
                _title = [Title(content=[media_object.name], lang=media_object.lang)]
                if media_object.info is not None:
                    if media_object.info.fullname is not None:
                        _title = [Title(content=[media_object.info.fullname], lang=media_object.lang)]
                if media_info_object is not None:
                    _category = [Category(content=[genre], lang=media_object.lang) for genre in media_info_object.genres.genres]
                    _credits = Credits(producer=media_info_object.productionCo.productionCo, writer=media_info_object.creators.creators)
                    _date = self.get_proper_date_time(media_info_object.releaseDate, _NEW_DATE_FORMAT_MINIMAL)
                    _desc = [Desc(content=[media_info_object.summary], lang=media_object.lang)]
                    _icon = [Icon(src=media_info_object.image)]
                    _rating = [xmltv.Rating(value=media_info_object.contentRating, system='VCHIP')]
                    _star_rating = [StarRating(value='{}/{}'.format(media_info_object.rating, 10), system='imdb')]
                    _sub_title = [SubTitle(content=[media_info_object.name], lang=media_object.lang)]
                    _title = [Title(content=[media_info_object.name], lang=media_object.lang)]
                    if media_info_object.episode is not None:
                        _desc = [Desc(content=[media_info_object.episode.summary], lang=media_object.lang)]
                        _episode_num = [EpisodeNum(content=['{}.{}.0/1'.format(media_info_object.episode.season - 1, media_info_object.episode.epNum - 1)], system='xmltv_ns')]
                        _sub_title = [SubTitle(content=[media_info_object.episode.name], lang=media_object.lang)]

                self.TV_OBJECT.programme.append(
                    Programme(
                        category=_category,
                        channel=media_object.channel,
                        clumpidx=None,
                        credits=_credits,
                        date=_date,
                        desc=_desc,
                        episode_num=_episode_num,
                        icon=_icon,
                        language=Language(content=[media_object.lang], lang=media_object.lang),
                        rating=_rating,
                        start=media_object.startDate,
                        star_rating=_star_rating,
                        stop=media_object.stopDate,
                        sub_title=_sub_title,
                        title=_title
                    )
                )
            except AttributeError as attributeException:
                self.LOGGER.error('Unable to add element: \n\t --Element: {} \n\t --Info Element: {} \n\t --Reason: {}.'.format(media_object, media_info_object, attributeException))

    def write_to_m3u_file(self, m3u_out_file: str):
        """
        Method that writes the loaded channels to an M3U file of your choosing.
        """
        self.LOGGER.debug('Writing channels to {}.'.format(m3u_out_file))
        m3u_text = '#EXTM3U\n'
        for channel in self.CHANNELS.element:
            channel_text = '\n#EXTINF:-0 channel-id="{}" tvg-name="{}" tvg-language="{}" tvg-country="{}" tvg-id"{}" tvg-logo="{}" group-title="{}"\n{}\n' \
                .format(
                    channel.id,
                    channel.displayName,
                    channel.lang,
                    channel.country,
                    channel.displayName,
                    channel.icon,
                    channel.group,
                    channel.url
                )
            m3u_text += channel_text
        open(m3u_out_file, 'w').write(m3u_text)

    def get_proper_date_time(self, date_time_string, new_format):
        """
        Simple Method to help get the current date format and then change
         the format to the desired format.
        :param date_time_string: The string to be re-formatted
        :param new_format: The new format the datetime will return
        :return: The new dateformat
        """
        self.LOGGER.debug('Converting the date_time_string {} to format {}.'.format(date_time_string, new_format))
        if date_time_string != '' and date_time_string is not None:
            if type(date_time_string) is datetime:
                return date_time_string.strftime(new_format)
            else:
                return parser.parse(date_time_string, fuzzy=True).__format__(new_format)


def main():
    ta = ToonamiAftermath()
    ta.main()


if __name__ == "__main__":
    main()
