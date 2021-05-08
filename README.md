# EE447Lab
Distributed Computing Platform


## Frontend Setup

- install [node.js](https://nodejs.org/en/), latest stable will be fine
- `cd frontend`
- `npm install --registry=https://registry.npm.taobao.org` to install dependencies

To test installation

- Compiles and hot-reloads for development `npm run serve`
- Visit `localhost:8080`

Misc

- Compiles and minifies for production `npm run build`
- [Vue.js DevTools](https://chrome.google.com/webstore/detail/nhdogjmejiglipccpnnnanhbledajbpd) Chrome Extension may facilitate developing


## Backend Setup

1. create a new venv
2. `pip install -r requirements.txt`
3. `python manage.py migrate`
4. `python manage.py createsuperuser`, create a super user (can be arbitrary, it only works on your local machine)

To test the installation

1. create a file `backend/secret.py` and write `secret="username:password"`
2. In three separate terminals, run the following in `backend` directory
   1. `python manage.py runserver`
   2. `celery -A backend.celery worker -l INFO -E` to start the server
   3. `celery -A backend.celery events -l info --camera django_celery_monitor.camera.Camera --frequency=2.0` to start the monitor
3. visit `localhost:8000/admin`, login with your previously set username `admin`, password `admin`
4. You should see an admin board provided by Django
5. visit `localhost:8000/api/test`, and check the admin board again, a test task will be seen

