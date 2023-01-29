#! c:/Python26/python.exe
# -*- coding: utf-8 -*-
#100 knock No.18
# writer:edagawa
#written 2016/04/07

col1=[]
f = open("hightemp.txt","r")
lines = f.readlines()
f.close()
for i in range(len(lines)):
    col1.append(lines[i].split())
for j in range(len(lines)/2):
    col1[j],col1[-j-1]=col1[-j-1],col1[j]
print col1

