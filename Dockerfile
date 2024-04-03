# syntax=docker/dockerfile:1

FROM python

WORKDIR /python-docker

COPY requirements.txt requirements.txt
COPY app.py app.py
RUN pip install -r requirements.txt

COPY . .

CMD [ "python", "app.py" ]
