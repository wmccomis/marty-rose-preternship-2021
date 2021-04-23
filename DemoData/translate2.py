#!/usr/bin/env python3

import sys
import re
import os

cnt=[]
for line in open('/etc/passwd', 'r'):
    field=line.split(':')[4]
    if 'User' in field or 'user' in field:
        cnt.append(field)
print(len(cnt))
