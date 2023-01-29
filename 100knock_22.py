#! c:/Python26/python.exe
# -*- coding: utf-8 -*-
#100 knock No.21
# writer:edagawa
#written 2016/06/19

import re
import json

f = open("jawiki-country.json","r")

for i in range(300):
    jsonData = f.readline()
    jsonstring = json.loads(jsonData)
    #print jsonstring["title"]
    if jsonstring["title"] == "イギリス":
        UK = jsonstring["text"]
        #print UK
        break

f.close()

pattern = r"={2,4}([^=\s]*)={2,4}"
iterator = re.finditer(pattern,UK)
for match in iterator:
    category = match.groups()[0].decode("utf-8")
    print category