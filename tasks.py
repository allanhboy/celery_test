# -*- coding: utf-8 -*-
import os

from celery import Celery

env_dict = os.environ
broker = env_dict.get('BROKER', 'redis://localhost:6379/1')
app = Celery('tasks', broker=broker)


@app.task
def crawl_keywords(what):
    print(what)


if __name__ == '__main__':
    app.start()
