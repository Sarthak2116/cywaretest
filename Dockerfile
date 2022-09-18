FROM alpine


RUN apk add nginx;

COPY index.html /var/www/localhost/htdocs/index.html

# adding nginx configuration
ADD default.conf /etc/nginx/conf.d/default.conf

# adding keys and certs
ADD $PWD/configs/*.key /etc/ssl/private/
ADD $PWD/configs/*.crt /etc/ssl/certs/
WORKDIR /var/www/localhost/htdocs

# ENTRYPOINT
COPY entrypoint.sh /usr/local/bin
RUN chmod +x /usr/local/bin/entrypoint.sh
ENTRYPOINT ["/bin/sh", "/usr/local/bin/entrypoint.sh"]

EXPOSE 80
EXPOSE 443

CMD ["/bin/sh", "-c", "nginx -g 'daemon off;'; nginx -s reload;"]