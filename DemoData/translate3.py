#!/usr/bin/env python3

# Luis Sosa Manubes

import sys
import requests
import re

URL= 'http://yld.me/raw/Hk1'

data=requests.get(URL).text
regexObj=re.compile(r'^B.*')

match=[]
for line in data.splitlines():
    if line.split(',')[1]:
        f2=line.split(',')[1]
        if re.match(regexObj, f2):
            match.append(f2)

for name in sorted(match):
    print(name)
