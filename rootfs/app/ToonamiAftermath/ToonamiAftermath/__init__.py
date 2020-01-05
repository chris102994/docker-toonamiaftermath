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

    gist_enabled = os.getenv('GIT_ENABLED')
    if gist_enabled is not None or gist_enabled is 'TRUE':
        first_run = os.getenv('FIRST_RUN')
        if first_run is 'TRUE':
            tools.curl_to_gist('ToonamiAftermath.m3u', '/data/ToonamiAftermath/ToonamiAftermath.m3u')
            os.environ['FIRST_RUN'] = 'FALSE'
            
        tools.curl_to_gist('Toonami_Aftermath_Guide.xml', file_name)

    else:
        print('Pushing to Gist Is not enabled.')


if __name__ == "__main__":
    main()
