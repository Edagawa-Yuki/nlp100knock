#! c:/Python26/python.exe
# -*- coding: utf-8 -*-
#100 knock No.13
# writer:edagawa
#written 2016/03/31

col1=""
col2=""
col12=""
f = open("col1+col2.txt","w")
g=open('col1.txt','r')
h=open('col2.txt','r')
col1=g.readlines()
col2=h.readlines()
for i in range(len(col1)):
    line = col1[i].split()[0] + " " + col2[i]
    print line
    f.write(line)
g.close()
h.close()
f.close()
