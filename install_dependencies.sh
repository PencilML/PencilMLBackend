#!/bin/bash

conda install pytorch torchvision -c pytorch
conda install matplotlib opencv pillow scikit-learn scikit-image
conda install -c anaconda flask==1.0.3 flask-cors
conda install -c conda-forge connexion