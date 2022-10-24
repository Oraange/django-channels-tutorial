FROM python:3.9

LABEL maintainer="hrpp1100@gmail.com"
LABEL version="1.0.0"
LABEL description="Django Channels Chatting Service"

WORKDIR /home/channels
COPY requirements.txt ./

RUN apt-get update
RUN apt-get install vim -y
RUN apt-get install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8818

CMD ["gunicorn", "--bind", "0.0.0.0:8818", "socket_channels.asgi:application", "--reload"]