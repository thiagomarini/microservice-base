import httplib, jwt
from config import JWT_SECRET, JWT_AUDIENCE
from datetime import datetime, timedelta


def create_auth_header(payload={}):
    return {'Authorization': create_jwt_bearer(jwt_encode(payload))}


def jwt_encode(payload):
    payload['exp'] = datetime.utcnow() + timedelta(days=1)
    payload['aud'] = JWT_AUDIENCE
    return jwt.encode(payload, JWT_SECRET, algorithm='HS256').decode('utf-8')


def jwt_decode(encoded_token):
    return jwt.decode(encoded_token, JWT_SECRET, algorithms=['HS256'], audience=JWT_AUDIENCE)


def create_link_header(uri, rel, title):
    return '<' + uri + '>; rel="' + rel + '"; title="' + title + '"'


def create_jwt_bearer(encoded_token):
    return "Bearer {0}".format(encoded_token)
