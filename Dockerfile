FROM pypy:3

RUN apt-get update &&\
    apt install build-essential libuv1-dev libssl-dev -y &&\
    apt-get remove -y --purge build-essential && \
    apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/*

RUN mkdir api

COPY requirements.txt ./api

RUN pypy3 -m pip install -r /api/requirements.txt

WORKDIR /api

COPY app ./app

EXPOSE 3000

CMD [ "pypy3", "./app/main.py" ]