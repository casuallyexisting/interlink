#
# Interlink Server
#   (c) 2021 Mason Coles
#   For local use
#

import os
import sys
import time
import json
import socket
import pylzma
import psutil
import logging
from threading import Thread
from subprocess import Popen, PIPE

# vars
seen_clients = []
current_directory = os.getcwd()
cfg = json.load(open('config.json', 'r'))

# Logging Configuration
logging.basicConfig(
    format="[%(levelname)-8s]: %(asctime)s - LINK -   %(message)s", datefmt="%m/%d/%Y %H:%M:%S", level=logging.INFO,
)
logger = logging.getLogger(__name__)

logger.debug('ADDRESS = {}:{}'.format(cfg['address'], cfg['port']))
logger.info('Ready.')

# Socket Configuration
sock = socket.socket()
sock.bind((cfg['address'], cfg['port']))
sock.listen(1)


while True:
    # Login Sequence
    while True:
        client, addr = sock.accept()
        client.send(b'Interlink v0.1.0')
        user = client.recv(1024)
        while not user:
            user = client.recv(1024)
        user = user.decode()

        passwd = client.recv(1024)
        while not passwd:
            passwd = client.recv(1024)
        passwd = passwd.decode()
        if user in cfg['username'] and passwd in cfg['password']:
            client.send(b"Login successful -- Don't forget to log out")
            logger.info('User connected: ' + user + ' - ' + addr[0])
            connected_addr = addr[0]
            break
        else:
            client.send(b'Login Failed.')

    # Main Code
    while True:
        client, addr = sock.accept()
        if addr[0] != connected_addr:
            client.send(b'Invalid Session')
            break
        logger.debug('STATUS: PAIRED')
        request = client.recv(1024)
        request = request.decode()

        if request == 'logout':
            client.send(b'Goodbye!')
            logger.info('User disconnected: ' + user)
            break

        cur_dir = os.path.dirname(os.path.realpath(__file__))
        os.chdir(cur_dir)

        request = request.split(' ')
        try:
            command = ['python', request[0] + '.py', request[1]]
        except:
            command = ['python', request[0] + '.py']
        process = Popen(command, stdout=PIPE)

        # Read pid from logfile
        with open('pid.log', 'rb') as f:
            time.sleep(1)
            process = f.read()
        with open('pid.log', 'wb') as f:
            f.write(b'')

        if request[0] != 'kill':
            client.sendall(b'Started process ' + process)
            logger.info("Process " + process.decode() + " started.")
            process = Popen(['python', cur_dir + '\\check_alive.py', process.decode()], stdout=PIPE)
            logger.debug('STATUS: WAITING TO PAIR')
        else:
            client.sendall(b'Killed process ' + request[1].encode('utf-8'))
