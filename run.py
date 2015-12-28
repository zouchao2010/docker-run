# -*- coding: utf-8 -*-
import sys
import os

import time

count = 0
while count < 50:
    count += 1
    f = open('run.log', 'a+')
    if count == 0:
        f.write("Start........PID:{}\n".format(os.getpid()))
    elif count == 50:
        f.write("Stop.........PID:{}\n".format(os.getpid()))
    else:
        f.write("Run..........PID:{}.....Count:{}\n".format(os.getpid(), count))
    f.close()
    time.sleep(1)
sys.exit(0)
