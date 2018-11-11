# GAE Python micro service boilerplate

A project boilerplate for GAE the micro services with JWT support.

## In a nutshell:

* It uses [Flask](http://flask.pocoo.org/) as it's web framework.
* It comes with an Account model and endpoints in `rest_api_v1.py` to create and fetch accounts.
The idea is that to start consuming the service you should have an account and any URI should start with the account ID.
* It uses [Halogen](https://pypi.python.org/pypi/halogen) to represent data in HAL format.
* To validate json payloads it uses [json_payload_validator](https://pypi.org/project/json_payload_validator/).
* Also the request are guarded by the `guard_request` function using [JWT](https://pyjwt.readthedocs.io/en/latest/).
* There is also the `manual_tests.py` file you should use to test stuff manually.
* It comes with [Jinja2](http://jinja.pocoo.org/docs/dev/) set up although it's not used.

**IMPORTANT:** change the values of `JWT_SECRET` and `JWT_AUDIENCE` on the `config.py` file. 

## How to use

Use virtual env for development:
- `pip install virtualenv`
- `virtualenv venv`
- `source venv/bin/activate`
- `pip install -r requirements.txt -t lib`

## Testing

Install [nosegae](https://pypi.org/project/NoseGAE/) `pip install nosegae`

Run tests `nosetests --with-gae tests/`
