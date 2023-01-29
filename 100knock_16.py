#! c:/Python26/python.exe
# -*- coding: utf-8 -*-
#100 knock No.16
# writer:edagawa
#written 2016/04/05

N = input('分割する行数=')
f = open("hightemp.txt","r")
line = f.readlines()
f.close()
row = len(line)/N
print row
for i in range(row):
    print line[i]