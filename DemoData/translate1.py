#!/usr/bin/env python3
# Luis Sosa Manubes

import sys
import os
import re

regex=re.compile(r'9\d*9')
match=re.findall(regex, open('/etc/passwd').read())
print(len(match))
