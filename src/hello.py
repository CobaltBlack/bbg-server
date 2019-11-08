import os
import sys

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
    PC_MAC_ADDR = '1C:1B:0D:61:ED:B5'
    CMD_WAKEUP = 'sudo etherwake -i eth0 {} &>> /var/log/wake.log'.format(PC_MAC_ADDR)
    app.logger.info('Executing wakeup: {}'.format(CMD_WAKEUP))
    os.system(CMD_WAKEUP)
    return 'OK'


if __name__ == "__main__":
    app.run()
else:
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger = gunicorn_logger
