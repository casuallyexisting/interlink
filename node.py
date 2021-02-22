#
# Interlink Node
#   (c) 2021 Mason Coles
#   For local use
#

import os
import socket
import logging
import time
import sys

# vars
cfg = json.load(open('node-config.json', 'r'))

# Logging Configuration
logging.basicConfig(
    format="[%(levelname)-8s]: %(asctime)s - NODE -   %(message)s", datefmt="%m/%d/%Y %H:%M:%S", level=logging.DEBUG)
logger = logging.getLogger(__name__)


def send(command):
    sock = socket.socket()
    sock.connect((cfg['address'], cfg['port']))
    data = sock.recv(16384)
    data = data.decode()
    sock.sendall(b'panel')
    sock.sendall(b'InterlinkControlPanel')
    response = sock.recv(16384)
    sock.close()

    sock = socket.socket()
    sock.connect((cfg['address'], cfg['port']))
    sock.sendall(command.encode('utf-8'))
    time.sleep(1)
    data = sock.recv(16384)
    data = data.decode()
    print('\n< ', data + '\n')
    sock.close()

    # Log Out
    sock = socket.socket()
    sock.connect((cfg['address'], cfg['port']))
    sock.sendall(b'logout')
    time.sleep(1)
    data = sock.recv(16384)
    data = data.decode()
    sock.close()
