# -*- coding: utf-8 -*-
from celery import Celery

app = Celery('tasks')

@app.task
def crawl_keywords(what):
    print(what)

if __name__ == '__main__':
    app.start()