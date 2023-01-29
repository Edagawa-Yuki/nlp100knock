#! c:/Python26/python.exe
# -*- coding: utf-8 -*-
#100 knock No.12
# writer:edagawa
#written 2016/03/27

col1 = ''
f = open("hightemp.txt","r")
g = open('col1.txt','w')
h = open('col2.txt','w')
lines = f.readlines()
f.close()
for i in range(len(lines)):
    line = lines[i].replace('\t',' ')
    g.write(line.split()[0] + '\n')
    h.write(line.split()[1] + '\n')
print col1
g.close()
h.close()