#! c:/Python27/python.exe
# -*- coding: utf-8 -*-
#100 knock No.19
# writer:edagawa
#written 2016/04/08

m = 0
group = set([])
f = open("col1.txt","r")
lines = f.readlines()
for i in range(len(lines)):
    group.add(lines[i].rstrip("\n"))
for x in group:
    print(x)
count = [0 for i in range(len(group))]
for j in range(len(group)):
    if lines[1] in group:
        m = m+1
print m
f.close()
