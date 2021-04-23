#!/usr/bin/env python3
import os
ls=os.popen('ls').read()

for script in ls:
#    print(script)
    if 'file' in script:
        os.popen(f'cp {script}')



