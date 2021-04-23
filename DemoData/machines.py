#!/usr/bin/env python3

import requests
import re
# Constants

URL = 'http://catalog.cse.nd.edu:9097/query.json'

# TODO: Make a HTTP request to URL
response = requests.get(URL)

# TODO: Access json representation from response object
data = response.text

# TODO: Display all machine names with type "wq_factory"
reg=re.compile(r'{"name":"([^"]+)".*"type":"wq_factory".*')

for machine in re.findall(reg, data):
	print(machine)
