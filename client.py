import json

import requests

payload = {'username': 'admin', 'password': 'admin', 'appcode': '1234567890'}
remote_base_url = "http://ec2-54-218-179-22.us-west-2.compute.amazonaws.com:9000/"
local_base_url = "http://localhost:9000/"
login_url = remote_base_url + "login"
asset_url = remote_base_url + "admin/asset"
collection_url = remote_base_url + "admin/collection/"
document_url = remote_base_url + "document/"
session = requests.session()
session_keys = {}
query = {}


def authenticate():
    r = session.post(login_url, data=payload)
    session_keys['X-BB-SESSION'] = r.headers['X-BB-SESSION']


def create_asset(data):
    r = session.post(asset_url, data=data)


def create_collection(name):
    session.headers = {'X-BB-SESSION': session_keys['X-BB-SESSION']}
    r = session.post(collection_url + name)
    print(r.text)


def create_document(collection, data):
    if document_available(collection, data):
        print("{} : Available".format(data['title']))
    else:
        session.headers = {'X-BB-SESSION': session_keys['X-BB-SESSION'], 'Content-Type': 'application/json'}
        r = session.post(document_url + collection, data=json.dumps(data))
        id = json.loads(r.text)['data']['id']
        print("{} : Added".format(data['title']))
        grant_document_access(collection, id, "registered")


def grant_document_access(collection, id, role):
    session.headers = {'X-BB-SESSION': session_keys['X-BB-SESSION']}
    r = session.put(document_url + collection + "/" + id + "/update/role/" + role)


def document_available(collection, data):
    session.headers = {'X-BB-SESSION': session_keys['X-BB-SESSION']}
    query['where'] = "{}='{}'".format('title', data['title'])
    r = session.get(document_url + collection, params=query)
    response = json.loads(r.text)
    if response['data']:
        body = data['body']
        if response['data'][0]['body']['day'] == body['day'] and \
                        response['data'][0]['body']['start_time'] == body['start_time'] and \
                        response['data'][0]['body']['location'] == body['location']:
            return True
    else:
        return False


        # authenticate()
        # print(document_available('athitt', dict(title="DEV310A")))
