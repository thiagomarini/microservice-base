import unittest, re, json, logging
from google.appengine.ext import testbed, ndb

from models import Account

def extract_uri_from_link_header(link_header):
    rex = re.compile(r'<(.*?)>', re.S | re.M)
    match = rex.match(link_header)
    if match:
        return match.groups()[0].strip()
    raise ValueError('Could not extract uri from: ' + link_header)


class AppTestBase(unittest.TestCase):
    ACCOUNT_USERNAME = 'account_username'

    def setUp(self):
        # First, create an instance of the Testbed class.
        self.testbed = testbed.Testbed()
        # Then activate the testbed, which prepares the service stubs for use.
        self.testbed.activate()
        # Next, declare which service stubs you want to use.
        self.testbed.init_datastore_v3_stub()
        self.testbed.init_blobstore_stub()
        self.testbed.init_memcache_stub()
        self.testbed.init_taskqueue_stub()
        self.testbed.init_app_identity_stub()
        self.testbed.init_urlfetch_stub()
        # Clear ndb's in-context cache between tests.
        # This prevents data from leaking between tests.
        # Alternatively, you could disable caching by
        # using ndb.get_context().set_cache_policy(False)
        ndb.get_context().clear_cache()

    def _create_account(self):
        account = Account(username=self.ACCOUNT_USERNAME)
        return account.put()
