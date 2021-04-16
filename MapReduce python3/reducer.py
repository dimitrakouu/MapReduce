#!/usr/bin/env python3
import sys


prevInfo ,prevIp, count = None,None, 0

for v in sys.stdin:
    v = v.strip()
    info = v.split(',')

    if (info[0] == prevIp):
        if (info[1] != prevInfo):
            count += 1
            prevInfo =info[1]
        else:
            continue
    else:
        if prevIp:
            print (prevIp, count)
        count = 1
        prevIp = info[0]
        prevInfo = info[1]

if prevIp == info[0]:
    print (prevIp, count) 
