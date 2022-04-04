FROM python:3.10.4-slim-bullseye

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONASYNCIODEBUG 1
ENV PYTHONTRACEMALLOC 1

RUN mkdir -p /home/cli && addgroup cli && useradd -d /home/cli -g cli cli && chown cli:cli /home/cli
RUN apt-get update && apt-get install -y curl
USER cli
WORKDIR /home/cli
ENV POETRY_HOME=/tmp/poetry
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python - --no-modify-path
ENV PATH=$POETRY_HOME/bin:$PATH
RUN poetry config virtualenvs.create false
ENV PATH=/home/cli/.local/bin:$PATH

COPY ./pyproject.toml ./poetry.lock ./
RUN poetry install --no-root --no-dev

COPY ./pyproject.toml /home/cli/.local/lib/python3.10/site-packages/pyproject.toml
COPY ./cli ./cli/
RUN pip install .

ENTRYPOINT [ "sleep", "infinity" ]