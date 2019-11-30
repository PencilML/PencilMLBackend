FROM continuumio/miniconda3

# install deps
RUN conda install --yes --freeze-installed \
    --channel pytorch --channel anaconda --channel conda-forge \
    pytorch torchvision \
    matplotlib opencv pillow scikit-learn scikit-image \
    flask==1.0.3 connexion \
    && conda clean -afy \
    && find /opt/conda/ -follow -type f -name '*.a' -delete \
    && find /opt/conda/ -follow -type f -name '*.pyc' -delete \
    && find /opt/conda/ -follow -type f -name '*.js.map' -delete