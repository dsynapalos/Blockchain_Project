def test_import_datetime():
    import datetime
    assert datetime.datetime.now()

def test_import_hashlib():
    import hashlib
    assert hashlib.md5

def test_import_json():
    import json
    assert json.loads('1')

def test_import_flask():
    import flask
    assert flask.Flask(__name__)