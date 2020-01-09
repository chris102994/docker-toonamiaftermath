import os
from datetime import date

from ToonamiAftermath.helpers import Tools
from ToonamiAftermath.toonami_aftermath import ToonamiAftermathGuideScraper


def main():
    url_episodes = 'https://api.toonamiaftermath.com/media?scheduleName=Toonami%20Aftermath%20EST&dateString={}&count=150'.format(date.today())

    scraper = ToonamiAftermathGuideScraper()
    channel_list = scraper.get_channels()
    est_episode_list = scraper.get_episodes(url_episodes, "+0000", "Toonami Aftermath EST")
    est_episode_list = scraper.link_episodes(est_episode_list)

    pst_episode_list = scraper.get_episodes(url_episodes, "-0300", "Toonami Aftermath PST")
    pst_episode_list = scraper.link_episodes(pst_episode_list)

    episode_list = est_episode_list + pst_episode_list

    file_name = '/data/ToonamiAftermath/Toonami_Aftermath_Guide.xml'
    tools = Tools()
    tools.wrapper(file_name=file_name, channel_list=channel_list, episode_list=episode_list)


if __name__ == "__main__":
    main()
