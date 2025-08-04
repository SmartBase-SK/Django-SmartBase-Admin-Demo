FROM docker.elastic.co/elasticsearch/elasticsearch:7.17.10

RUN /usr/share/elasticsearch/bin/elasticsearch-plugin install analysis-icu

COPY ./config /usr/share/elasticsearch/config
RUN chown -R elasticsearch:elasticsearch /usr/share/elasticsearch/config
