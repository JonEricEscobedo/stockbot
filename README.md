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
Run the Vue.js frontend (from the app folder) in one terminal window:
```
yarn dev
```
Run the backend in a second terminal window:
```
dev_appserver.py .
```

## Deploy
From `/app`:
```
cd app
yarn build
```
`cd..` back out to root and run:
```
gcloud app deploy app.yaml
```

## Deployed
[Stockbot](https://stockbot-196406.appspot.com/)

## Notes
`main.py` code credit for Google App Engine and Flask + Vue compatibility goes to: https://github.com/Valmoz/gae-vue-flask-starter.
This repo was incredibly helpful getting Flask + Vue ready for GAE deployment.
