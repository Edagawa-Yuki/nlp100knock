#! c:/Python26/python.exe
# -*- coding: utf-8 -*-
#100 knock No.05
# writer:edagawa
# from 2015/9/13 to 2015/9/...

#"paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．

A = "paraparaparadise"
B = "paragraph"
X=[]
Y=[]
for i in range(0,len(A)-1):
    X.append(A[0+i:2+i])
print X

for i in range(0,len(B)-1):
    Y.append(B[0+i:2+i])
print Y

for i in range(0,len(X)-2):
    for j in range(i+1,len(X)-1):
        if X[i+1]==

Sum=[]
Pro=[]
DifX=[X[x] for x in range(0,len(X))]
DifY=[Y[y] for y in range(0,len(Y))]
for k in range(0,len(X)):
    for l in range(0,len(Y)):
        if X[k]==Y[l]:
            Pro.append(X[k])
            print 1
            #del DifX[k]
            #del DifY[l]

#Sum = Pro + DifX + DifY
#print Sum
print Pro
#print DifX
#print DifY
