'''
Channel Object Data Class
'''


class ChannelObject:
    title: str
    url: str
    icon_url: str

    def __init__(self, title: str, url: str, icon_url: str):
        self.title = title.replace(' ', '%20')
        self.url = url
        self.icon_url = icon_url

    def to_string(self):
        return '    <channel id="{}">\n' \
               '        <display-name lang="en">{}</display-name>\n' \
               '        <icon src="{}"/>\n' \
               '        <url>{}</url>\n' \
               '    </channel>\n' \
                .format(self.title, self.title, self.icon_url, self.url)


'''
Program Object Data Class
'''


class ProgramObject:
    title: str
    icon_url: str
    start_time: str
    time_offset: str
    end_time: str
    channel_number: str
    episode_name: str
    date: str
    block_name: str

    def __init__(self, title: str, icon_url: str, start_time: str, time_offset: str,
                 end_time: str, channel_number: int, episode_name: str, date: str, block_name: str):
        self.title = title
        self.icon_url = icon_url
        self.start_time = start_time
        self.time_offset = time_offset
        self.end_time = end_time
        self.channel_number = channel_number.replace(' ', '%20')
        self.episode_name = episode_name
        self.date = date
        self.block_name = block_name

    def to_string(self):
        return '    <programme start="{} {}" stop="{} {}" channel="{}">\n' \
               '        <title lang="en">{}</title>\n' \
               '        <sub-title lang="en">{}</sub-title>\n' \
               '        <date>{}</date>\n' \
               '        <icon src="{}"/>\n' \
               '        <category lang="en">{}</category>\n' \
               '    </programme>\n' \
                .format(self.start_time, self.time_offset, self.end_time, self.time_offset, self.channel_number,
                        self.title, self.episode_name, self.date, self.icon_url, self.block_name)