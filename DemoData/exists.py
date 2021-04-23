#!/usr/bin/env python3

import sys
import os.path

for arg in sys.argv[1:]:
	if(os.path.exists(arg)==1):
		print(f'{arg} exists!')
	else:
		print(f'{arg} does not exist!')
		sys.exit(1)
sys.exit(0)
