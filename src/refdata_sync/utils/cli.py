import sys


def fatal(msg):
    sys.stderr.write(msg + '\n')
    sys.exit(1)
