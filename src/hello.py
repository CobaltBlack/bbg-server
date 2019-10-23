import os

from flask import Flask, request
app = Flask(__name__)

import logging

@app.route('/')
def hello_world():
    app.logger.info('info visited')
    return 'Hello, World!'
    
@app.route('/wakeup', methods=['POST'])    
def wake_up():
    app.logger.info('wakeup called')
    # Call script to perform wakeup
    os.system('~/wakeup &>> /var/log/wake.log')
    return 'OK'

if __name__ == "__main__":
    app.run()
else:
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger = gunicorn_logger
