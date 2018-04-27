# -*- coding:utf-8 -*-

from __future__ import absolute_import
from celery import Celery
# from celery.signals import after_task_publish

app = Celery('schedule',include=['schedule.tasks'])
app.config_from_object('schedule.celery_config')

if __name__ == '__main__':
    app.start()
