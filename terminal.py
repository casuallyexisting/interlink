#
# Interlink Terminal
#   (c) 2021 Mason Coles
#   For local use
#

import os
import socket
import logging
import time
from getpass import getpass

# vars
cfg = json.load(open('node-config.json', 'r'))

# Logging Configuration
logging.basicConfig(
    format="[%(levelname)-8s]: %(asctime)s - TERM -   %(message)s", datefmt="%m/%d/%Y %H:%M:%S", level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Login
while True:
    sock = socket.socket()
    sock.connect((cfg['address'], cfg['port']))
    data = sock.recv(16384)
    data = data.decode()
    print('\n' + data)
    user = input('Username: ')
    sock.sendall(user.encode('utf-8'))
    passwd = getpass()
    sock.sendall(passwd.encode('utf-8'))
    response = sock.recv(16384)
    print(response.decode(), '\n')
    if response == b"Login successful -- Don't forget to log out":
        break

sock.close()

# Main Code
while True:
    command = input(">  ").encode('utf-8')
    sock = socket.socket()
    sock.connect((cfg['address'], cfg['port']))
    sock.sendall(command)
    time.sleep(1)
    data = sock.recv(16384)
    data = data.decode()
    if data:
        print('< ', data + '\n')
        if data == 'Goodbye!':
            break
    sock.close()
