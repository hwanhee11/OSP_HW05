#!/usr/bin/python

import sys

f = open(sys.argv[1],'r')
n = int(sys.argv[2])

lines = f.readlines()
lines = [line.strip() for line in lines]