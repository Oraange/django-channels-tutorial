# Django Channels Test Repository

## 실시간 채팅 기능

### Web Socket을 이용하여 실시간 채팅 기능 구현

- [Django-Channels 공식 문서](https://channels.readthedocs.io/en/stable/index.html)를 참고하여 만들었음
  - `django-channels-tutorial/chat/async_consumers.py` 및 `django-channels-tutorial/chat/sync_consumers.py`에 웹소켓 통신 코드 작성
  - `async_consumers.py`는 비동기 consumer, `sync_consumers.py`는 동기 consumer를 구현한 것이다. 자세한 내용은 [공식 문서의 Consumers](https://channels.readthedocs.io/en/stable/topics/consumers.html) 참고
<br>

- url
  - `http://localhost:8000/chat`
  - `http://localhost:8000/chat/<room_name>`

## 실시간 알림 기능

### Web Socket을 이용하여 실시간 알림 기능 구현

- 실시간 채팅 기능을 기반으로 state에 따른 project의 색이 실시간으로 변경되도록 구현
- url
  - `http://localhost:8000/users/signup`
  - `http://localhost:8000/users/signin`
  - `http://localhost:8000/projects`



## 실행 방법

> 로컬 실행 방법

```sh
# Change to the directory where you want to work in
$ git clone https://github.com/Oraange/django-channels-tutorial.git

$ cd django-channels-tutorial

$ python manage.py runserver

# Please install docker
$ docker run --name <container name> -p 6379:6379 -d redis:5

# Create your environment file
$ touch env.json

$ vim env.json

# Start Server
$ python manage.py runserver
```

- `env.json` 작성 예시
```json
{
    "SECRET_KEY": "<Sceret Key>",
    "DATABASES": {
        "default": {
            "ENGINE": "<DB engine>",
            "NAME": "<DB name>",
            "USER": "<User name>",
            "PASSWORD": "<Password>",
            "HOST": "<Host IP>",
            "PORT": "<DB Port>",
            "TEST": {
                "NAME": "<User name>"
            }
        }
    },
    "CHANNEL_LAYERS_HOSTS": {
        "LOCAL": ["127.0.0.1", 6379]
    },
    "WEBDRIVER": "<Webdriver path>"
}
```
