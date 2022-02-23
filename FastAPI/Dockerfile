FROM python:3.10-slim

# set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y netcat

COPY . /FastAPI

# set work directory
WORKDIR /FastAPI

# install dependencies
RUN pip install -r app/requirements.txt

CMD ["sh", "/FastAPI/entrypoint.sh"]
