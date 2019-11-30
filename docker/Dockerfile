FROM continuumio/miniconda3

# clone the project
RUN git clone https://github.com/PencilML/PencilMLBackend.git /opt/PencilMLBackend

# setup analitics
ENV PENCIL_ML_ANALYTICS_MODELS_DIR /opt/PencilMLBackend/analitics/models
ENV PENCIL_ML_ANALYTICS_MODEL_NAME dextr_pascal-sbd
ADD dextr_pascal-sbd.pth /opt/PencilMLBackend/analitics/models

# setup web
ENV PENCIL_ML_WEB_DEXTR_IMAGE_UPLOAD_FOLDER /opt/PencilMLBackend/web/upload

# install deps
RUN conda install --yes --freeze-installed \
    --channel pytorch --channel anaconda --channel conda-forge \
    nomkl \
    torchvision \
    matplotlib opencv pillow scikit-learn scikit-image \
    flask==1.0.3 connexion \
    && conda clean -afy \
    && find /opt/conda/ -follow -type f -name '*.a' -delete \
    && find /opt/conda/ -follow -type f -name '*.pyc' -delete \
    && find /opt/conda/ -follow -type f -name '*.js.map' -delete

# expose web server port
EXPOSE 8080

ENTRYPOINT ["/opt/conda/bin/python", "/opt/PencilMLBackend/server_runner.py"]