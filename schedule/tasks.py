# -*- coding:utf-8 -*-

from __future__ import absolute_import
from .app import app
from nbu_cmd.nbu_cmd import nbu_start_or_stop,get_policys

@app.task
def test_task():
    return 'test success'

@app.task
def nbu_start_or_stop_task(params):
    return nbu_start_or_stop(params)

@app.task
def get_policys_task():
    return get_policys()

