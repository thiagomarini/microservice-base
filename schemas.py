import json

import halogen
from flask import url_for


class AccountSchema(halogen.Schema):
    self = halogen.Link(attr=lambda account: url_for("get_account",
                                                     account_key=account.key.urlsafe()))
    id = halogen.Attr(attr=lambda account: account.key.id())
    username = halogen.Attr()
