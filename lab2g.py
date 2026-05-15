#!/usr/bin/env python3
# Author: Joshua Luczon
# Author ID: jluczon
# Date Created: May 15, 2026

import sys

if len(sys.argv) >= 2:
    timer = int(sys.argv[1])
else:
    timer = 3

while timer > 0:
    print(timer)
    timer = timer - 1
print('blast off!')
