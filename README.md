## [chris102994/docker-toonamiaftermath](https://github.com/chris102994/docker-toonamiaftermath)

[![https://www.toonamiaftermath.com/](https://vignette.wikia.nocookie.net/toonami/images/0/0f/Toonami_aftermath_logo.png/revision/latest?cb=20121120205018)](https://www.toonamiaftermath.com/)

[![Build Status](https://travis-ci.com/chris102994/docker-toonamiaftermath.svg?branch=master)](https://travis-ci.com/chris102994/docker-toonamiaftermath)
[![Microbadger Size & Layers](https://images.microbadger.com/badges/image/christopher102994/docker-toonamiaftermath.svg)](https://microbadger.com/images/christopher102994/docker-toonamiaftermath)
[![Image Pulls](https://img.shields.io/docker/pulls/christopher102994/docker-toonamiaftermath)](https://hub.docker.com/repository/docker/christopher102994/docker-toonamiaftermath)
[![Alpine](https://images.microbadger.com/badges/version/christopher102994/docker-toonamiaftermath:alpine-3.10-latest.svg)](https://microbadger.com/images/christopher102994/docker-toonamiaftermath:alpine-3.10-latest)


[Toonami Aftermath](https://www.toonamiaftermath.com/) is a Toonami revival effort, which began as a 24/7 stream, launched on January 18, 2010 with its website appearing a few months after that. It airs programs that have been broadcast on Toonami, and also Cartoon Network, Fox, and Kids WB, such as Ronin Warriors, Cartoon Cartoons, X-Men: The Animated Series, and Pokemon. 

I do not officially endorse the Toonami Aftermath project or its affiliates. 

This is a simple project that scrapes the website and generates an M3U playlist every 12 hours along with a XMLTV object that is hosted over NGINX.

The XMLTV and M3U playlist can be directly imported to Emby or Plex. Or if you'd like a buffer you can also import them into xteve or tvheadend. 


## Docker
```
docker run \
	--name=docker-toonamiaftermath \
	-p 8000:8000 \
	-v </path/to/appdata/config>:/config \
	--restart unless-stopped \
	christopher102994/docker-toonamiaftermath:alpine-3.10
```

## Parameters
Container specific parameters passed at runtime. The format is `<external>:<internal>` (e.g. `-p 443:22` maps the container's port 22 to the host's port 443).

| Parameter | Function |
| -------- | -------- |
| -p 8000 | This is the port inside the container by default however, you can map the outside port to be the same as the inner port. (Default 8000)  |
| -v /config | The directory where the application will store configuration information. |
| -e USERNAME | The Username you wish to run as. (Optional) |
| -e GROUPNAME | The Groupname you wish to run as. (Optional) |
| -e PUID | The UID you wish to run and save files as. (Optional) |
| -e PGID | The GID you wish to run and save files as. (Optional) |
| -e LOG_LEVEL | The Python Logging log level for the TA Scraper. (Default ERROR) |
| -e USE_EPISODE_CACHE | Cache the episode data that is scraped from TA. This will make future runs faster. (Default True)|
| -e GUIDE_ITEMS_PER_CHANNEL | The number of guide items to get for each channel. This grabs guide items from the beginning of the day. If too low then it might not grab enough to see. If too high then it will take a long time to do the first run. (Default 200) |

## Application Setup

The basic index is available at `http://<ip>:<port>/`

This will build and allow you to point your M3U Tuner to `http://<ip>:<port>/ToonamiAftermath.m3u`
and your XEPG tuner to `http://<ip>:port/ToonamiAftermathGuide.xml`
