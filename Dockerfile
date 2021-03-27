# pull official base image
FROM python:3
LABEL maintainer="Rodrigo" 
ENV PYTHONUNBUFFERED 1
RUN mkdir /DjangoRest
WORKDIR /DjangoRest
RUN pip install --upgrade pip
COPY requirements.txt /DjangoRest/
RUN pip install -r requirements.txt
COPY . /DjangoRest/
