#! c:/Python26/python.exe
# -*- coding: utf-8 -*-
#100 knock No.08
# writer:edagawa
#written 2015/11/2

def cipher(x):
    if ord(x)>=ord("a") and ord(x)<=ord("z"):
        y=219-ord(x)
        return chr(y)
    else:
        return x

print cipher("b")
