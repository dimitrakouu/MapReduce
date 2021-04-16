#!/usr/bin/env python3
import sys


prevInfo ,prevIp, count = None,None, 0

for v in sys.stdin:
    v = v.strip()
    ips, info = v.split(',')

    if (ips == prevIp):
        if (info != prevInfo):
            count += 1
            prevInfo =info
        else:
            continue
    else:
    	if prevIp:
    	    print(prevIp, count)
    	count = 1
    	prevIp = ips
    	prevInfo = info

if prevIp == ips:
    print(prevIp, count) 
