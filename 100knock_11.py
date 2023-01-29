#! c:/Python26/python.exe
# -*- coding: utf-8 -*-
#100 knock No.11
# writer:edagawa
#written 2016/03/15

f = open("hightemp.txt","r")
line = f.readlines()
f.close()
for i in range(len(line)):
    print(line[i].replace('\t',' '))