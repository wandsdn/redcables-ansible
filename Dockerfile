FROM debian:stretch

RUN \
  apt-get update && \
  apt-get install -qy --no-install-recommends \
    python \
    python-dev \
    python3 \
    python3-dev \
    build-essential \
    ca-certificates \
    supervisor

RUN sed -i 's/^\(\[supervisord\]\)$/\1\nnodaemon=true/' /etc/supervisor/supervisord.conf
