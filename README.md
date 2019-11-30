# Install

1) Install conda
2) Run install_dependencies.sh

# Project structure

## Analytics

Contains all classes that responsive for Deep Extreme Cut (DEXTR) algorithm

Runner: dextr_runner.py

## Web server

Runner: server.py  
127.0.0.1:8080/swagger-ui

## Docker

https://hub.docker.com/r/scrat98/pencil-ml-backend  
docker run -dit -p 8080:8080 scrat98/pencil-ml-backend