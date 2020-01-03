 
## [chris102994/docker-toonamiaftermath]()

[Toonami Aftermath](https://www.toonamiaftermath.com/) is a Toonami revival effort, which began as a 24/7 stream, launched on January 18, 2010 with its website appearing a few months after that. It airs programs that have been broadcast on Toonami, and also Cartoon Network, Fox, and Kids WB, such as Ronin Warriors, Cartoon Cartoons, X-Men: The Animated Series, and Pokemon. 

I do not officially endorse the Toonami Aftermath project or its affiliates. 

This is a simple project that scrapes the website and generates an m3u playlist along with a XmlTV guide that can be stored locally or on a github GIST so that live tv players such as Emby or Plex can view the channels. 

 [![Build Status](https://travis-ci.com/chris102994/docker-toonamiaftermath.svg?branch=master)](https://travis-ci.com/chris102994/docker-toonamiaftermath)

## Outside Packages
* Built on my [Base GUI Image](https://github.com/chris102994/docker-toonamiaftermathi)


## Docker
```
docker run \
	--name=docker-toonamiaftermath \
	-e GIT_ENABLED:TRUE `optional` \
	-e GITHUB_API_URL:<your gist url> `optional` \
	-e GITHUB_API_TOKEN:<your github api token> `optional` \
	-v </path/to/appdata/config>:/config \
  	-v </path/to/data>:/data \
	--restart unless-stopped \
	christopher102994/docker-toonamiaftermath
```

## Parameters
Container specific parameters passed at runtime. The format is `<external>:<internal>` (e.g. `-p 443:22` maps the container's port 22 to the host's port 443).

| Parameter | Function |
| -------- | -------- |
| -e GIT_ENABLED | If you want to post results on a gist set to TRUE (Default=FALSE). |
| -e GITHUB_API_URL | If GIT_ENABLED then you need a new GIST URL. |
| -e GITHUB_API_TOKEN | If GIT_ENABLED then you need a Github API Token to enable pushing. |
| -v /config | The directory where the application will store configuration information. |
| -v /data | The path where the m3u playlist and XmlTV guide generated will be stored. |
