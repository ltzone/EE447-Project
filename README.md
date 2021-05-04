# EE447Lab
Distributed Computing Platform


## Frontend Setup

- install [node.js](https://nodejs.org/en/), latest stable will be fine
- `cd frontend`
- `npm install --registry=https://registry.npm.taobao.org` to install dependencies
- Compiles and hot-reloads for development `npm run serve`
- Compiles and minifies for production `npm run build`
- [Vue.js DevTools](https://chrome.google.com/webstore/detail/nhdogjmejiglipccpnnnanhbledajbpd) Chrome Extension may facilitate developing


## Backend Setup

1. create a new venv
2. `pip install -r requirements.txt`
3. `python manage.py migrate`
4. `python manage.py runserver`
5. `celery -A backend.celery worker -l INFO` to start the server

Seems to be an easy way to setup broker and database

```
docker run -d -p 5672:5672 rabbitmq
```

