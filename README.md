# Flask+Firebase Authentication+Nginx+MySQL docker-compose

## FirebaseのProject URL
- https://console.firebase.google.com/project/accountmanager-a05b4

## 起動コマンドとか
- docker-compose build
- docker-compose up -d

## 停止
- docker-compose down

## Status
- docker-compose ps


## log確認
- docker logs {コンテナ名}
- docker logs flask-docker_python_1

## コンテナログイン
- docker-compose exec db bash


## 参考URL
- https://qiita.com/kenkono/items/6221ad12670d1ae8b1dd
- https://qiita.com/trrrrrys/items/a905f1382733dfb9c8c1



## DB
### login
- docker-compose exec db bash
- mysql -u user -p
  - password

### database list
- SHOW DATABASES;
- use test;
- show tables;


## API 動作確認
### ユーザ一覧
- curl --location --request GET 'http://localhost:4231/api/users'

### ユーザ登録
curl --location --request POST 'http://localhost:4231/api/users' \
--header 'Content-Type: application/json' \
--data-raw '{
  "name": "山田太郎",
  "address":"茨城県つくば市千現",
  "tel":"02812345678",
  "mail":"blogtest@swallow-incubate.com"
}'

