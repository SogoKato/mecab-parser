FROM python:3.9-slim-bullseye

WORKDIR /var/app

RUN apt update \
    && apt install -y \
    g++ git make curl sudo file xz-utils \
    mecab libmecab-dev \
    && cd /var \
    && git clone https://github.com/neologd/mecab-ipadic-neologd.git --depth=1 \
    && cd mecab-ipadic-neologd \
    && ./bin/install-mecab-ipadic-neologd -y -n -a \
    && pip install \
    flask==2.0.2 \
	mecab-python3==1.0.4 \
	uwsgi==2.0.20 \
    && export SUDO_FORCE_REMOVE=yes \
	&& apt remove -y \
    g++ git make curl sudo file xz-utils \
    libmecab-dev \
    && apt autoremove -y \
    && apt clean \
    && rm -rf /var/lib/apt/lists/* \
    && rm -rf /var/mecab-ipadic-neologd

COPY . .

ENV MECABRC=/etc/mecabrc

CMD ["uwsgi", "--yaml", "/var/app/uwsgi.yaml"]
