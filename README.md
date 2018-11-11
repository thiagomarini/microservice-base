# GAE Python micro service boilerplate

[![License: MPL 2.0](https://img.shields.io/badge/License-MPL%202.0-brightgreen.svg)](https://opensource.org/licenses/MPL-2.0)

Boilerplate for GAE micro services with JWT support.
The idea is that to start consuming the service you should have an account first and any API resources would live inside the account ID.
Example: 
- `/ACCOUNT-ID/users`
- `/ACCOUNT-ID/users/posts`
- `/ACCOUNT-ID/tags`

## In a nutshell:

* It uses [Flask](http://flask.pocoo.org/) as it's web framework.
* It comes with an Account model and endpoints in `rest_api_v1.py` to create and fetch accounts.
* It uses [Halogen](https://pypi.python.org/pypi/halogen) to represent data in HAL format.
* To validate json payloads it uses [json_payload_validator](https://pypi.org/project/json_payload_validator/).
* Requests are guarded by the `guard_request` function using [JWT](https://pyjwt.readthedocs.io/en/latest/).
* There is a `manual_tests.py` file should need to test stuff manually.
* Although [Jinja2](http://jinja.pocoo.org/docs/dev/) is set up it's not used.

**IMPORTANT:** change the values of `JWT_SECRET` and `JWT_AUDIENCE` on the `config.py` file before using it.

## How to use

Use virtual env for development:
- `pip install virtualenv`
- `virtualenv venv`
- `source venv/bin/activate`
- `pip install -r requirements.txt -t lib`

## Testing

Install [nosegae](https://pypi.org/project/NoseGAE/) `pip install nosegae`

Run tests `nosetests --with-gae tests/`
