# uoffice hosting on GCP groddkeeper project uoffice service
辦公室值日生通知系統

https://uoffice-dot-groddkeeper.wl.r.appspot.com

## 值日生排班用Google Sheet

https://docs.google.com/spreadsheets/d/1hqTdgDqiisX-MoHjRmPxgrax7ocD8g70SPAZBzJORe0

## GAE service deploy command
$ gcloud app deploy app.yaml --project groddkeeper

## GAE cron deploy command
$ gcloud app deploy cron.yaml

## Visit the Cloud Platform Console Task Queues page to view your queues and cron jobs.
https://console.cloud.google.com/appengine/taskqueues/cron?project=groddkeeper

## uoffice service architecture
![uoffice](https://raw.githubusercontent.com/FLHCoLtd/uoffice/main/uoffice.jpg?raw=true|width=640)


## 說明 
開發策略：分支開發，主線發布
引用元件：主線發布時，透過`app-yaml-env-compiler` gh-action 動態設定 GAE `app.yaml` 內的 `env_variables` 參數
其他服務：Cloud Scheduler for GAE Cron
