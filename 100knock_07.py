#! c:/Python26/python.exe
# -*- coding: utf-8 -*-
#100 knock No.07
# writer:edagawa
#written 2015/11/2

#引数x, y, zを受け取り「x時のyはz」という文字列を返す関数を実装せよ．さらに，x=12, y="気温", z=22.4として，実行結果を確認せよ．

def square(x,y,z):
    return str(x)+"時の"+y+"は"+str(z)

print square(12,"気温",22.4)
