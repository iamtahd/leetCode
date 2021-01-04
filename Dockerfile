FROM python:3.9

WORKDIR /leetCode

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .