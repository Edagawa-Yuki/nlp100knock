#! c:/Python26/python.exe
# -*- coding: utf-8 -*-
#100 knock No.03
# writer:edagawa, 2015/8/27

#Invert "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics." to pi

A = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
B=A.split(".")[0]
B=B.split(",")
B="".join(B)
C=B.split(" ")
print C
D=[]
for i in range(0,len(C)):
    D.append(len(C[i]))
print D
