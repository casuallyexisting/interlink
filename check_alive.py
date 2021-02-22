import logging
import psutil
import sys

pid = sys.argv[1]

# Logging Configuration
logging.basicConfig(
    format="[%(levelname)-8s]: %(asctime)s - LINK -   %(message)s", datefmt="%m/%d/%Y %H:%M:%S", level=logging.INFO,
)
logger = logging.getLogger(__name__)

while psutil.pid_exists(int(pid)):
    print('', end='', flush=True)
logger.info("Process " + pid + " killed.")
