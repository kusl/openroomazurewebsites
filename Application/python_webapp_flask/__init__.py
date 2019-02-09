"""
The flask application package.
"""

from os import environ

from applicationinsights.requests import WSGIApplication
from flask import Flask

app = Flask(__name__)
if "APPINSIGHTS_INSTRUMENTATIONKEY" not in environ:
    environ.__setitem__("APPINSIGHTS_INSTRUMENTATIONKEY", "blank")
app.wsgi_app = WSGIApplication(environ.get('APPINSIGHTS_INSTRUMENTATIONKEY'), app.wsgi_app)
import python_webapp_flask.views
