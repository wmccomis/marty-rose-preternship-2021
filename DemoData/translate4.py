#!/usr/bin/env python3
# Luis Sosa Manubes

import sys
import os
from collections import Counter

data=os.popen('/bin/ls -l /etc').read()

nums=sorted([line.split()[1] for line in data.splitlines()])
cnt=Counter(nums)

for key, value in cnt.items():
    print(f'{value:>7} {key}')
