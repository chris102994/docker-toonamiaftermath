
'''
Toonami TV Guide Scraper Class
'''
import json
import ssl
import sys
from urllib.request import urlopen

from ToonamiAftermath.data_classes import ProgramObject, ChannelObject


class  ToonamiAftermathGuideScraper:
    def __init__(self):
        pass

    def get_channels(self):
        channel_list = []
        est_name = 'Toonami Aftermath EST'
        pst_name = 'Toonami Aftermath PST'
        icon_url = 'https://vignette.wikia.nocookie.net/toonami/images/0/0f/Toonami_aftermath_logo.png/revision/latest?cb=20121120205018'
        url = 'https://www.toonamiaftermath.com/'

        obj = ChannelObject(est_name, url, icon_url)
        channel_list.append(obj)
        obj = ChannelObject(pst_name, url, icon_url)
        channel_list.append(obj)

        return channel_list

    def get_episodes(self, url, timeoffset, channelnumber):
        episode_list = []
        context = ssl._create_unverified_context()
        
        try:
            data = urlopen(url, context=context).read()
        except:
            print('Error getting guide. Check your connection and ensure that toonamiaftermath.com is up')
            sys.exit(1)

        json_data = json.loads(data)
            
        for media_type in json_data:
            name = media_type.get('name', '')
            startdate = media_type.get('startDate', '')
            # Nested Item
            info = media_type.get('info', '')
            if info != '':
                fullname = info.get('fullname', '')
                image = info.get('image', '')
                episode = info.get('episode', '')
            blockname = media_type['blockName']

            timesplit = startdate.split("T")
            date = timesplit[0].replace('-', '')
            starttime = timesplit[1].replace(':', '').replace('.', '').replace('Z', '')[:-3]
            starttime = date + starttime
            if fullname != '':
                name = fullname

            obj = ProgramObject(name, image, starttime, timeoffset, "", channelnumber, episode, date, blockname)
            episode_list.append(obj)

        return sorted(episode_list, key=lambda ProgramObject: ProgramObject.start_time)


    def link_episodes(self, episode_list):
        for i in range(0, len(episode_list)-1):
            if episode_list[i+1]:
                curObj = episode_list[i]
                nextObj = episode_list[i+1]
                curObj.end_time = nextObj.start_time

        return episode_list
