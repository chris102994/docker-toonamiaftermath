import os
from datetime import date

from ToonamiAftermath.helpers import Tools
from ToonamiAftermath.toonami_aftermath import ToonamiAftermathGuideScraper


def main():
    '''
    Common Data
    '''
    est_keyword = 'EST'
    pst_keyword = 'PST'
    est_offset = '+0000'
    pst_offset = '-0300'
    '''
    Toonami Aftermath Data
    '''
    ta_url_episodes = 'https://api.toonamiaftermath.com/media?scheduleName=Toonami%20Aftermath%20EST&dateString={}&count=150'.format(
        date.today())
    ta_url_icon = 'https://vignette.wikia.nocookie.net/toonami/images/0/0f/Toonami_aftermath_logo.png/revision/latest?cb=20121120205018'
    ta_channel_name = 'Toonami Aftermath'
    ta_est_channel_name = '{} {}'.format(ta_channel_name, est_keyword)
    ta_pst_channel_name = '{} {}'.format(ta_channel_name, pst_keyword)
    '''
    Snickelodeon Data
    '''
    sn_url_episodes = 'https://api.toonamiaftermath.com/media?scheduleName=Snickelodeon%20EST&dateString={}&count=150'.format(
        date.today())
    sn_url_icon = 'https://vignette.wikia.nocookie.net/ultraverse/images/a/a9/Cartoonverse_-_Nickelodeon_-3.png/revision/latest/scale-to-width-down/1000?cb=20200710152142'
    sn_channel_name = 'Snickelodeon'
    sn_est_channel_name = '{} {}'.format(sn_channel_name, est_keyword)
    sn_pst_channel_name = '{} {}'.format(sn_channel_name, pst_keyword)

    scraper = ToonamiAftermathGuideScraper()
    channel_list = channel_helper(scraper, ta_est_channel_name, ta_url_icon) + \
                   channel_helper(scraper, ta_pst_channel_name, ta_url_icon) + \
                   channel_helper(scraper, sn_est_channel_name, sn_url_icon) + \
                   channel_helper(scraper, sn_pst_channel_name, sn_url_icon)

    episode_list = episode_helper(scraper, ta_url_episodes, est_offset, ta_est_channel_name, ta_url_icon) + \
                   episode_helper(scraper, ta_url_episodes, pst_offset, ta_pst_channel_name, ta_url_icon) + \
                   episode_helper(scraper, sn_url_episodes, est_offset, sn_est_channel_name, sn_url_icon) + \
                   episode_helper(scraper, sn_url_episodes, pst_offset, sn_pst_channel_name, sn_url_icon)

    file_name = '/data/ToonamiAftermath/Toonami_Aftermath_Guide.xml'
    tools = Tools()
    tools.wrapper(file_name=file_name, channel_list=channel_list, episode_list=episode_list)


def channel_helper(scraper: ToonamiAftermathGuideScraper, channel_name: str, icon_url: str):
    channel_list = scraper.get_channels(channel_name, icon_url)
    return channel_list


def episode_helper(scraper: ToonamiAftermathGuideScraper, guide_url: str, time_offset: str, channel_name: str,
                   icon_url: str):
    this_episode_list = scraper.get_episodes(guide_url, time_offset, channel_name)
    this_episode_list = scraper.link_episodes(this_episode_list)
    return this_episode_list


if __name__ == "__main__":
    main()
