#!/bin/sh
# Lazy script to run app either in container or locally from root directory
# Usage: ./scripts/api.sh

# Configuration
dotenv="$(pwd)/app/dev.env"
image='barrettotte/pokemon-teams-app'
cont_name='pokemon-teams-app'
port=8021
app_src="$(pwd)/app"

local_run(){
  export $(cat $dotenv | xargs) # load env variables
  npm run --prefix $app_src serve -- --port $port
}

docker_run(){
  sudo docker build -t $image $app_src && \
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