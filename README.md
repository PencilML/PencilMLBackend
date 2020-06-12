# Pencil ML Backend  
  
## Prerequisites
- python3  
- conda  
  
## Installation
  
1) Install python linting tools: `pip install --user black isort flake8 mypy`  
2) Install pre-commit: `pip install --user pre-commit`  
3) Install pre-commit hook in repo: `pre-commit install` (in the project root dir)  
4) Initialize conda environment: `conda env create -n pencil-ml-backend -f environment.yml`  
5) Download DEXTR model: `scripts/get_model.sh`

## Running  

### Run locally

`conda run python -m backend`

Local running requires you to manually setup environment variables declared in `docker-compose.yml`
and copy data files to the appropriate directories, so this is not a recommended way to run the app.
Please refer to **Run in Docker** section for seamless running instructions.

### Run in Docker
1) Install Docker using your package manager of choice (e.g. `apt install docker`)
2) *OPTIONAL:* Follow Docker [post-installation steps](https://docs.docker.com/install/linux/linux-postinstall/)
3) Install docker-compose: `pip install --user docker-compose`
4) Run the app: `docker-compose --compatibility up` (use `sudo` if neccessary)

## Modules

### Analytics

Contains all classes that responsive for Deep Extreme Cut (DEXTR) algorithm

Runner: dextr_runner.py

### Web server

Runner: server_runner.py  
127.0.0.1:8080/swagger-ui

## References
This repo with made with using of https://github.com/scaelles/DEXTR-PyTorch
