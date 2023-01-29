#! c:/Python26/python.exe
# -*- coding: utf-8 -*-
#100 knock No.14
# writer:edagawa
#written 2016/04/04

N = input('表示する行数=')
f = open("hightemp.txt","r")
line = f.readlines()
f.close()
for i in range(N):
    print line[i]