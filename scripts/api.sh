#!/bin/sh
# Lazy script to run API either in container or locally from root directory
# Usage: ./scripts/api.sh

# Configuration
dotenv="$(pwd)/api/dev.env"
image='barrettotte/pokemon-teams-api'
cont_name='pokemon-teams-api'
port=8020
api_src="$(pwd)/api"

local_run(){
  export $(cat $dotenv | xargs) # load env variables
  python3 $api_src/src/app.py
}

docker_run(){
  sudo docker build -t $image $api_src && \
  sudo docker run -d --env-file $dotenv -p $port:$port --rm --name $cont_name $image
  # (add -it for interactive)
}

if [ $# -eq 0 ]; then
  local_run
else
  case "$1" in
    -d|-docker ) docker_run ;;
    -l|-local  ) local_run  ;;
    *) echo "Invalid option [ (-d|-docker) (-l|-local)]" ;;
  esac
fi