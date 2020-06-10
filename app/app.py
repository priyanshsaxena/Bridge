#!/usr/bin/env python
"""Flask base-code

Uses Flask.
"""

from flask import Flask

__author__ = "Priyansh Saxena"
__credits__ = ["Priyansh Saxena"]
__license__ = "GPL"
__version__ = "0.1.0"
__email__ = "askpriyansh@gmail.com"
__status__ = "Non-Production"

App = Flask(__name__)


@App.route('/')
def index():
	return "Hello World"


if __name__ == '__main__':
	App.run(debug=True)
