# -*- coding:utf-8 -*-

from __future__ import absolute_import
from .app import app

@app.task
def test_task(params):
    test_json = {
        'params':params
    }
    import json
    return json.dumps(test_json)

