#! c:/Python26/python.exe
# -*- coding: utf-8 -*-
#100 knock No.17
# writer:edagawa
#written 2016/04/06

col1=set([])
print col1
f = open("col1.txt","r")
lines = f.readlines()
for i in range(len(lines)):
    col1.add(lines[i].rstrip("\n"))
    print col1
for x in col1:
    print(x)