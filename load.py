import sys
import os
from time import sleep
import json
import logging
from subprocess import Popen, PIPE

# Logging Configuration
logging.basicConfig(
    format="[%(levelname)-8s]: %(asctime)s - LOAD -   %(message)s", datefmt="%m/%d/%Y %H:%M:%S", level=logging.INFO,
)
logger = logging.getLogger(__name__)

with open('pid.log', 'wb') as f:
    f.write(str(os.getpid()).encode('utf-8'))

args = sys.argv

cfg = json.load(open('config.json', 'r'))

args = args[1].split('/')

os.chdir(cfg['dir'] + args[0])
logger.info(os.getcwd())
file = ''
if len(args) > 2:
    for block in args[1:-1]:
        file += "/" + block
file += args[-1]
process = Popen(['python', file + '.py'], stdout=PIPE)
#imported = getattr(__import__(cfg['dir'] + 'exo\\interfaces', fromlist=[name]), name)

while True:
    sleep(100)
