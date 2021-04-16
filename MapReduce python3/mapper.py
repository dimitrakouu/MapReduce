#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
mapper

"""

import sys

for record in sys.stdin:
    record = record.strip().split(',')

    if record[0] == "ip":
        continue
    else:
        ids = record[0]
        date = record[1]
        time = record[2][:5]
        ips = '%s' % (ids)
        info = ', %s %s %s' % (ids , date, time)
        print(ips, info)
        