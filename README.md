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

