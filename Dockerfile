FROM python:3

WORKDIR /app/fixed-width-to-csv-converter

COPY . .

RUN chmod 755 docker-cmd.sh

CMD ./docker-cmd.sh
