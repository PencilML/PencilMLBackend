FROM docker.pkg.github.com/enjoy-the-science/base-images/pencil-ml-backend AS base

WORKDIR /opt/PencilMLBackend
EXPOSE 8080


FROM base AS app

COPY ./backend ./backend
CMD ["conda", "run", "python", "-m", "backend"]


FROM base AS dev

COPY . .
RUN conda env update -f environment.yml && conda clean -afy
# Install additional dev deps that are not available in conda
RUN conda run pip install -r dependencies.dev
