# -*- coding: utf-8 -*-
"""
Create a mapper:  
keeps from log files the Ip -date- time

Create a reducer:
    Calculate remaining time of users(ids)

"""
from mrjob.job import MRJob


class IdsTrimmingCounter(MRJob):
    #define the mapper
    
    def mapper(self, key, record):
        record = record.strip().split(',')
        if record[0] == "ip":
            return
        else:
           ids= record[0]
           date = record[1]
           time = record[2][:5]
           info = '%s' % (ids)
           yield info, (ids, date, time)

    def reducer(self, info, ids_list):
        prev, count = None, 0
        for v in ids_list:
            if (v != prev):
                count += 1
                prev = v
        yield info, count


if __name__ == '__main__':
    IdsTrimmingCounter.run()
    