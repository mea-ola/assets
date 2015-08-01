FROM debian

RUN apt-get update -y
RUN apt-get install -y blender git python3 nginx

COPY ./ /assets
RUN rm -rf /etc/nginx/
COPY ./conf/nginx.conf /etc/nginx/nginx.conf

WORKDIR /assets
COPY entrypoint.sh /bin/entrypoint.sh
ENTRYPOINT /bin/entrypoint.sh
