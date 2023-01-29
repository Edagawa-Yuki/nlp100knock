#! c:/Python26/python.exe
# -*- coding: utf-8 -*-
#100 knock No.00
# writer:edagawa, 2015/8/27

# Get strings inversed "stressed"
from numpy import arange

A = 'stressed'
B = ''

for i in arange(8):
    j = 7-i
    B+=A[j]
print B
