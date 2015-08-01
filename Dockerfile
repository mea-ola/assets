FROM debian

RUN apt-get update -y
RUN apt-get install -y blender git python3 nginx

COPY entrypoint.sh /bin/entrypoint.sh
ENTRYPOINT /bin/entrypoint.sh
