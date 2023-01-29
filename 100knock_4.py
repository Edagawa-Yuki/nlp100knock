#! c:/Python26/python.exe
# -*- coding: utf-8 -*-
#100 knock No.04
# writer:edagawa, 2015/8/30

#Split "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can." by words, and pick up 1 or 2 words from each of them to be the periodic table.

A = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
B=A.split(".")
B="".join(B)
B=B.split(",")
B="".join(B)
B=B.split(" ")
C=[]
for i in range(1,len(B)+1):
    if i == 1 or i ==5 or i == 5 or i == 6 or i == 7 or i == 8 or i == 9 or i == 15 or i == 16 or i == 19:
        C.append(B[i-1][0])
    else:
        C.append(B[i-1][0:2]) 
print C

D={}
for j in range(0,len(C)):
    D.update({C[j]:j})
print D
    
