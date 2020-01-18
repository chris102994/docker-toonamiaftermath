# Pull the base image	
FROM christopher102994/docker-xteve:alpine-3.10
MAINTAINER chris102994<chris102994@yahoo.com>

ARG BUILD_DATE
ARG VERSION
ARG VCS_REF
LABEL org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.vcs-url="https://github.com/chris102994/docker-toonamiaftermath"
# Add Local Files
COPY rootfs/ /

# Setup Base Script
RUN	echo "##### Downloading Runtime Packages #####" && \
		install \
			zip && \
	echo "##### Downloading pip Packages #####" && \
		pip3 install -r /app/ToonamiAftermath/requirements.txt && \
	echo "##### Creating folders #####" && \
		mkdir -p \
			/data/ToonamiAftermath && \
	echo "##### Cron setup #####" && \
		# Execute the cron job every 2 hours at 15 mins after.
		echo "15	*/2	*	*	*	/app/ta-wrapper.sh >> /config/log/ToonamiAftermath.log" >> /etc/crontabs/root
ENV PYTHONPATH=/app/ToonamiAftermath/
ENV FIRST_RUN=TRUE
