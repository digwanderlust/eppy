#! /usr/bin/env python
"""clean up .pyc from folders"""
import sys, os, stat
from bsdopendirtype import opendir

def clean(path):
    global count
    try:
        content = opendir(path)
    except OSError:
        print >> sys.stderr, "skipping", path
        return
    for filename, smode in content:
        if stat.S_ISDIR(smode):
            clean(filename)
            if filename.endswith('/__pycache__'):
                try:
                    os.rmdir(filename)
                except OSError:
                    pass
        elif (filename.endswith('.pyc') or filename.endswith('.pyo') or
              filename.endswith('.pyc~') or filename.endswith('.pyo~')):
            os.unlink(filename)
            count += 1

count = 0

for arg in sys.argv[1:] or ['.']:
    print "cleaning path", arg, "of .pyc/.pyo/__pycache__ files"
    clean(arg)

print "%d files removed" % (count,)
