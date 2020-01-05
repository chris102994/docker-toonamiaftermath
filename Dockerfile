# Pull the base image	
FROM christopher102994/docker-base-img:alpine-3.10
MAINTAINER chris102994<chris102994@yahoo.com>

ARG BUILD_DATE
ARG VERSION

# Add Local Files
COPY rootfs/ /

# Setup Base Script
RUN	echo "##### Downloading Runtime Packages #####" && \
		apk add --no-cache \
			python3 && \
	echo "##### Downloading Virtual Build Dependencies #####" && \
		apk add --no-cache --virtual=build-dependencies \
			py3-pip && \
	echo "##### Downloading pip Packages #####" && \
		pip3 install -r /app/ToonamiAftermath/requirements.txt && \
	echo "##### Creating folders #####" && \
		mkdir -p \
			/data/ToonamiAftermath && \
	echo "##### Cron setup #####" && \
		# Execute the cron job every 2 hours at 15 mins after.
		echo "15	*/2	*	*	*	/app/ta-wrapper.sh >> /config/log/ToonamiAftermath.log" >> /etc/crontabs/root && \
	echo "##### Cleaning Up #####" && \
		apk del --purge build-dependencies
ENV PYTHONPATH=/app/ToonamiAftermath/
ENV FIRST_RUN=TRUE
