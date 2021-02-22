import os, signal
import sys

to_kill = sys.argv[1]

with open('pid.log', 'wb') as f:
    f.write(str(os.getpid()).encode('utf-8'))

os.kill(int(to_kill), signal.SIGTERM)
