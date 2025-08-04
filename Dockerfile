FROM python:3.9-bullseye

RUN apt-get update -y

# Add requirements
ADD ./requirements.txt /srv/django_project/requirements.txt

# Install packages
RUN apt-get -o Acquire::Check-Valid-Until=false update -y && apt-get install -y gettext vim supervisor

# Install application requirements
RUN pip3 install gunicorn
RUN pip3 install psycopg
RUN pip3 install pywatchman

RUN TMP_DIR="$(mktemp -d)" && cd "$TMP_DIR" && wget https://github.com/facebook/watchman/releases/download/v2022.02.14.00/watchman-v2022.02.14.00-linux.zip && \
    unzip watchman-v2022.02.14.00-linux.zip && cd watchman-v2022.02.14.00-linux && mkdir -p /usr/local/{bin,lib} /usr/local/var/run/watchman && \
    cp bin/* /usr/local/bin && cp lib/* /usr/local/lib && chmod 755 /usr/local/bin/watchman && \
    chmod 2777 /usr/local/var/run/watchman

RUN pip3 install --exists-action=w -r /srv/django_project/requirements.txt

# Create django user, will own the Django app
RUN adduser --no-create-home --disabled-login --group --system django

RUN mkdir -p /srv/media-files

# Add code
ADD . /srv/django_project

WORKDIR /srv/django_project
