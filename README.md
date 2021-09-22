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
