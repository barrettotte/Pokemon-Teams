FROM python:3.6.6-slim-stretch
WORKDIR /usr/src/app
COPY requirements.txt .
RUN \
  apt-get update && \
  apt-get install unixodbc unixodbc-dev odbc-postgresql libpq-dev gcc g++ -y && \
  python3 -m pip install -r requirements.txt --no-cache-dir 
COPY src/ .
EXPOSE 8020
ENTRYPOINT ["python3", "app.py"]

# sudo docker build -t barrettotte/pokemon-teams-api .
# sudo docker run -it --env-file dev.env -p 8020:8020 --rm --name pokemon-teams-api barrettotte/pokemon-teams-api