#!/usr/bin/env python
"""SocketIO basic code.

Uses python-socketio.
"""

import socketio
import eventlet
from flask import Flask, render_template

__author__ = "Priyansh Saxena"
__credits__ = ["Priyansh Saxena"]
__license__ = "GPL"
__version__ = "0.1.0"
__email__ = "askpriyansh@gmail.com"
__status__ = "Non-Production"

sio = socketio.Server()
app = Flask(__name__)

@app.route('/')
def index():
    """Serve the client-side application."""
    return render_template('index.html')

@sio.on('connect')
def connect(sid, environ):
    print('connect ', sid)

@sio.on('my message')
def message(sid, data):
    print('message ', data)

@sio.on('disconnect')
def disconnect(sid):
    print('disconnect ', sid)

if __name__ == '__main__':
    # wrap Flask application with socketio's middleware
    app = socketio.WSGIApp(sio, app)

    # deploy as an eventlet WSGI server
    eventlet.wsgi.server(eventlet.listen(('', 8000)), app)