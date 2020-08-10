## Docker Notes - I forget commands a lot...

# Basic Build/Run
```sh
sudo docker build -t barrettotte/pokemon-teams-api .
sudo docker run -it --env-file ../dev.env -p 8020:5000 --rm --name pokemon-teams-api barrettotte/pokemon-teams-api
```


## Troubleshooting
```sh
sudo docker run -t -d barrettotte/pokemon-teams-api
sudo docker exec -it <container_id> sh
```


## Cleaning up
```sh
sudo docker stop (sudo docker ps -a -q)
sudo docker rm (sudo docker ps -a -q)
```