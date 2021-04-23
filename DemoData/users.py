#!/usr/bin/env python3

import csv

# Constants

PATH = '/etc/passwd'

# TODO: Loop through ':' delimited data in PATH and extract the fifth field
# (user description)
user_descriptions=[]
for row in csv.reader(open(PATH), delimiter=':'):
	user_description=row[4]
	if user_description:
		user_descriptions.append(user_description)

# TODO: Print user descriptions in sorted order
for description in sorted(user_descriptions):
	print(description)
