FROM python:3.8
ENV PYTHONUNBUFFERED 1
RUN mkdir /var/www
# workdirの指定
WORKDIR /var/www
# 依存Pythonライブラリ一覧コピー
COPY requirements.txt ./
COPY uwsgi.ini ./
# 依存Pythonライブラリインストール
RUN pip install -r requirements.txt
# FIrebaseAuth用ライブラリのインストール
#RUN pip install git+https://github.com/jp-96/Flask-FirebaseAuth.git
WORKDIR /var/www/src
CMD ["uwsgi","--ini","/var/www/uwsgi.ini"]

