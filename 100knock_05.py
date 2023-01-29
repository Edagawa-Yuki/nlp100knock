#! c:/Python26/python.exe
# -*- coding: utf-8 -*-
#100 knock No.05
# writer:edagawa
# from 2015/9/11 to 2015/9/13

#Make the n-gram function from given sequences of letters or a list. Then, using this function, get a word bi-gram and a letter bi-gram from "I am an NLPer".

A = "I am an NLPer"
B=A.split(" ")
C=[]

for i in range(0,len(B)-1):
    C.append(" ".join(B[0+i:2+i]))
print C

B="".join(B)
D=[]
for j in range(0,len(B)-1):
    D.append(B[0+j:2+j])
print D
