import hmac, hashlib, httplib, logging, json
from flask import abort
from config import REQUEST_SALT


def create_link_header(uri, rel, title):
    return '<' + uri + '>; rel="' + rel + '"; title="' + title + '"'


def get_request_hash(request_data):
    # http://stackoverflow.com/questions/9652124/is-there-an-equivalent-of-phps-hash-hmac-in-python-django
    # PHP => hash_hmac("sha256", $request_data_string, REQUEST_SALT);
    request_data_string = json.dumps(request_data, separators=(',', ':'))  # use same separator as PHP!!
    return hmac.new(REQUEST_SALT, request_data_string, hashlib.sha256).hexdigest()


def create_auth_header(request_data):
    request_hash = get_request_hash(request_data)
    return {'Authorization': create_auth_value(request_hash)}


def create_auth_value(request_hash):
    return "AUTH {0}".format(request_hash)


def guard_request(request):
    request_values = request.values.to_dict()
    request_hash = get_request_hash(request_values)
    if 'Authorization' not in request.headers.keys():
        logging.warning('[Abort] Authorization header not found in request')
        abort(httplib.UNAUTHORIZED)
    auth_value = create_auth_value(request_hash)
    if request.headers['Authorization'] != auth_value:
        logging.warning('[Abort] Unauthorized request: ' + request.headers['Authorization'] + ' != ' + auth_value)
        abort(httplib.UNAUTHORIZED)
