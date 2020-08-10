# Tried to use alpine at first...I could not get this working... :(
# Keeping this for notes in the future

FROM python:3.6.5-alpine3.7
WORKDIR /usr/src/app
COPY requirements.txt .
RUN apk update
RUN \
  apk add --no-cache postgresql-libs unixodbc unixodbc-dev psqlodbc libstdc++ postgresql-dev && \
  apk add --no-cache --virtual .build-deps gcc g++ musl-dev && \
  python3 -m pip install -r requirements.txt --no-cache-dir && \
  apk --purge del .build-deps && \
  printf '[PostgreSQL Unicode]\nDriver=/usr/lib/psqlodbca.so\nSetup=/usr/lib/libodbcpsqlS.so' >> /etc/odbcinst.ini
COPY src/ .
EXPOSE 5000
ENTRYPOINT ["python3", "app.py"]

# sudo docker build -t barrettotte/pokemon-teams-api .
# sudo docker run -it --env-file dev.env -p 8020:5000 --rm --name pokemon-teams-api barrettotte/pokemon-teams-api