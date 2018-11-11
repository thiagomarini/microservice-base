from flask import abort
from util import jwt_decode
import logging
import httplib


class JwtMiddleware(object):
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        if 'HTTP_AUTHORIZATION' not in environ:
            logging.warning('[Abort] Authorization header not found in request')
            abort(httplib.UNAUTHORIZED)
        try:
            jwt_decode(environ['HTTP_AUTHORIZATION'].replace('Bearer ', ''))
        except Exception as e:
            logging.warning('JWT failed to decode')
            logging.warning(e)
            abort(httplib.UNAUTHORIZED)

        return self.app(environ, start_response)
