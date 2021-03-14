FROM alpine:3.9

COPY bin/backup /usr/local/bin/backup
COPY bin/crontab /var/spool/cron/crontabs/root
RUN chmod 700 /usr/local/bin/backup
RUN chmod 700 /var/spool/cron/crontabs/root

RUN apk add --no-cache mysql-client
ENTRYPOINT ["crond", "-f"]
