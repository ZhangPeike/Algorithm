#!/usr/bin/python
import os
import sys
import time
import json
from multiprocessing import Pool, Process

json_file = sys.argv[1]
fp=open(json_file,'r')
dataset_ID_list = json.load(fp)

def ProcessDataSet(cmd_name):
    print 'Run task %s(%s)' % (cmd_name, os.getpid())
    start=time.time()
    os.system(cmd_name)
    end=time.time()
    print 'Task %s run %0.3f sec.' % (cmd_name, (end-start))

mpool=Pool(10)
for i in range(10):
    config_name=str(i)
    cmd="echo "+config_name
    mpool.apply_async(ProcessDataSet, args=(cmd,))
mpool.close()
mpool.join()
print "All task is done."    