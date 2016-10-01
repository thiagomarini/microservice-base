import httplib, logging, json, io, os

from flask import Flask, request, abort, jsonify, url_for
from google.net.proto.ProtocolBuffer import ProtocolBufferDecodeError
import jinja2
from google.appengine.ext import ndb

from config import ROOT, ACCOUNTS
from models import Account
from schemas import AccountSchema
from util import get_request_hash, guard_request, create_link_header

app = Flask(__name__)

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

@app.route(ROOT, methods=['GET'])
def hello():
    guard_request(request)
    return 'my_app'


@app.route(ACCOUNTS, methods=['POST'])
def create_account():
    guard_request(request)
    # returns 400 Bad Request automatically if username is not present
    username = request.form['username']

    def create_existent_account_response():
        msg = 'Account already exists for username: ' + username
        link_header = create_link_header(
            url_for("get_account", account_key=account.key.urlsafe()),
            'account',
            msg
        )
        logging.warning(msg)
        return '', httplib.CONFLICT, {'Link': link_header}

    def create_new_account_response():
        new_account = Account(username=username)
        account_key = new_account.put()
        link_header = create_link_header(
            url_for("get_account", account_key=account_key.urlsafe()),
            'account',
            'Account created'
        )
        return '', httplib.CREATED, {'Link': link_header}

    account = Account.get_by_username(username)
    if account:
        return create_existent_account_response()
    return create_new_account_response()


@app.route(ACCOUNTS + '/<string:account_key>', methods=['GET'])
def get_account(account_key):
    guard_request(request)
    account = _get_entity(account_key)
    return jsonify(AccountSchema.serialize(account))


def _get_entity(entity_urlsafe_key):
    try:
        key = ndb.Key(urlsafe=entity_urlsafe_key)
        entity = key.get()
    except ProtocolBufferDecodeError:
        logging.info('Entity not found for key: %', entity_urlsafe_key)
        abort(httplib.NOT_FOUND)
    if not entity:
        abort(httplib.NOT_FOUND)
    return entity
