# Micro service base

The intention of this project is to create a base for the micro services I find myself creating all the time in GAE.

## In a nutshell:

* It uses [Flask](http://flask.pocoo.org/) as it's web framework.
* It comes with an Account model and endpoints in `rest_api_v1.py` to create and fetch accounts.
The idea is that to start consuming the service you should have an account and any URI should start with the account ID.
* It uses [Halogen](https://pypi.python.org/pypi/halogen) to represent data in HAL format.
* Also the request are guarded by the `guard_request` function using [HMAC](https://en.wikipedia.org/wiki/Hash-based_message_authentication_code), it basically creates a hash with the request payload so you can check if it was messed with. I recommend you don't rely only on it for security.
* Run `nosetests --with-gae tests/` in the app folder to run tests.
* There is also the `manual_tests.py` file you should use to test stuff manually.
