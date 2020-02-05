# Install

1) Install conda
2) Run install_dependencies.sh

# Project structure

Each module has config.py file for flexible configuration.

## Analytics

Contains all classes that responsive for Deep Extreme Cut (DEXTR) algorithm

Runner: dextr_runner.py

## Web server

Runner: server_runner.py  
127.0.0.1:8080/swagger-ui

# Deployment

## Docker build

base image - represent image with provisioning installed  
image - steps to install PencilMLBackends

## Docker start

https://hub.docker.com/r/scrat98/pencil-ml-backend  
docker run -dit -p 8080:8080 scrat98/pencil-ml-backend  
You have to allocate minimum 4gb of Ram!

# References
This repo with made with using of https://github.com/scaelles/DEXTR-PyTorch
