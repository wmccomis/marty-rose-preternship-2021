#!/usr/bin/env python3
# Luis Sosa Manubes

import collections
import re
import requests

# Globals

URL = 'https://cse.nd.edu/undergraduate/computer-science-course-map/'

# Initialize a default dictionary with integer values
counts = {'Sophomore' : 0, 'Junior' : 0, 'Senior' : 0}

# TODO: Make a HTTP request to URL
response = requests.get(URL)

# TODO: Access text from response object
data = response.text

# TODO: Compile regular expression to match CSE courses (ie. CSE XXXXX)
regex = re.compile(r'CSE [234][0-9]{4}')

# TODO: Search through data using compiled regular expression and count up all
# the courses per class year
for course in re.findall(regex, data):
    if course.startswith('CSE 2'):
	    counts['Sophomore'] = counts['Sophomore'] + 1
    elif course.startswith('CSE 3'):
	    counts['Junior'] = counts['Junior'] + 1
    elif course.startswith('CSE 4'):
	    counts['Senior'] = counts['Senior'] + 1

# Sort items in counts dictionary by value in reverse order and display counts
# and class year
for year, count in sorted(counts.items(), key=lambda p: p[1], reverse=True):
    print(f'{count:>7} {year}')
