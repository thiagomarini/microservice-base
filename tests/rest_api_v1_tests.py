from webtest import TestApp
from datetime import datetime
import httplib, json, logging
from rest_api_v1 import app
from config import ROOT, ACCOUNTS
from tests.app_test_base import AppTestBase, extract_uri_from_link_header
from util import create_auth_header, get_request_hash

app = TestApp(app)


def get(url, params={}):
    return app.get(url, headers=create_auth_header(params), expect_errors=True)


def post(url, params):
    return app.post(url,
                    params=params,
                    headers=create_auth_header(params),
                    expect_errors=True)


class ApiV1Test(AppTestBase):
    now = unicode(datetime.now())

    def test_authentication(self):
        response = get(ROOT, {'invalid': 'value'})
        self.assertEqual(response.status_int, httplib.UNAUTHORIZED)

    def test_api_root(self):
        response = get(ROOT)
        self.assertEqual(response.status_int, httplib.OK)
        self.assertEqual(response.normal_body, 'my_app')
        self.assertEqual(response.content_type, 'text/html')

    def test_creating_account_fails_if_username_is_not_provided(self):
        response = post(ACCOUNTS, {})
        self.assertEqual(response.status_int, httplib.BAD_REQUEST)

    def test_it_creates_account(self):
        response = self._hit_create_account_endpoint()
        self.assertEqual(response.status_int, httplib.CREATED)
        self.assertTrue(response.headers['Link'])

    def test_it_does_not_create_new_account_if_exists(self):
        self._hit_create_account_endpoint()
        response = self._hit_create_account_endpoint(True)
        self.assertEqual(response.status_int, httplib.CONFLICT)

    def test_account_exists(self):
        response1 = self._hit_create_account_endpoint()
        resource_uri = extract_uri_from_link_header(response1.headers['Link'])
        self._assert_account_resource(get(resource_uri))

    def _assert_account_resource(self, response):
        self._assert_OK_json_response(response)
        resource = json.loads(response.body)
        self.assertTrue(resource['id'])
        self.assertTrue(resource['username'])
        self.assertTrue(resource['_links']['self'])

    def _hit_create_account_endpoint(self, expect_errors=False):
        params = {'username': self.ACCOUNT_USERNAME}
        return post(ACCOUNTS, params)

    def _assert_OK_json_response(self, response):
        self.assertEqual(response.status_int, 200)
        self.assertEqual(response.content_type, 'application/json')
