# Stockbot

## Installing dependencies
Backend Flask dependencies (from root):
```
pip install -t lib -r requirements.txt
```
Frontend Vue.js dependencies (from the app folder):
```
yarn install
```
## Local development
Run the Vue.js frontend (from the app folder) in one termianl window:
```
yarn dev
```
Run the backend in a second terminal window:
```
dev_appserver.py .
```

## Deployed
[Stockbot](https://stockbot-196406.appspot.com/)

## Notes
`main.py` code credit for Google App Engine and Flask + Vue compatability goes to: https://github.com/Valmoz/gae-vue-flask-starter. 
This repo was increadibly helpful getting Flask + Vue ready for GAE deployment.
