# Accidents on Brazilian Federal Highways

<div align="center">
    <img src="https://cdn-icons-png.flaticon.com/512/1964/1964422.png" width="150"></img>
</div>

An API to get crash data from federal highways in Brazil using socketify.py and mongoDB.

## Dados

The data used are from a public source and make available by the Federal Highway Police (PRF) and are available at this [link](https://www.gov.br/prf/pt-br/acesso-a-informacao/dados-abertos/dados-abertos-acidentes). For this case, we used the base that groupped by occurrence, given any year (as long as the columns *latitude* and *longitude* exists).

## Virtualenv

```bash
# Create
virtualenv venv -p pypy3

# Activate
source venv/bin/activate
```

## Docker

```bash
# Docker Compose
docker-compose up --build

# Docker image - API
docker build -t accidents-api .
docker run -it -p 3000:3000 accidents-api 

# Docker image - MongoDB
docker run -d --name accidents_db \
 -e MONGO_INITDB_ROOT_USERNAME=mongoadmin \
 -e MONGO_INITDB_ROOT_PASSWORD=secret \
 -p 27017:27017 \
 mongo:4.0
```

## Install Packages

Install new packages using pypy3

```bash
pypy3 -m pip install <package-name>
```
