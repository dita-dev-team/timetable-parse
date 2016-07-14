import json

import requests

payload = {'username': 'admin', 'password': 'admin', 'appcode': '1234567890'}
base_url = "http://localhost:9000/"
login_url = base_url + "login"
asset_url = base_url + "admin/asset"
collection_url = base_url + "/admin/collection/"
document_url = base_url + "document/"
session = requests.session()
session_keys = {}


def authenticate():
    r = session.post(login_url, data=payload)
    session_keys['X-BB-SESSION'] = r.headers['X-BB-SESSION']


def create_asset(data):
    r = session.post(asset_url, data=data)


def create_collection(name):
    r = session.post(collection_url + name)
    print(r.text)


def create_document(collection, data):
    session.headers = {'X-BB-SESSION': session_keys['X-BB-SESSION'], 'Content-Type': 'application/json'}
    r = session.post(document_url + collection, data=json.dumps(data))
    id = json.loads(r.text)['data']['id']
    print(r.text)
    grant_document_access(collection, id, "registered")


def grant_document_access(collection, id, role):
    session.headers = {'X-BB-SESSION': session_keys['X-BB-SESSION']}
    r = session.put(document_url + collection + "/" + id + "/update/role/" + role)
    print(r.text)
