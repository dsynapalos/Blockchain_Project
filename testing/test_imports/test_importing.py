def test_import_datetime():
    import datetime
    assert datetime.datetime.now()


def test_import_hashlib():
    import hashlib
    assert hashlib.md5


def test_import_json():
    import json
    assert json.loads('1')


def test_import_requests():
    import requests
    assert requests


def test_import_flask():
    from uuid import uuid4
    assert uuid4()


def test_import_flask():
    import flask
    assert flask.Flask(__name__)


def test_import_flask():
    from urllib.parse import urlparse
    assert urlparse
