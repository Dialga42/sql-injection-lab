FROM mysql/mysql-server:5.6

ENV MYSQL_DATABASE weblab

COPY ./scripts/ /docker-entrypoint-initdb.d/
