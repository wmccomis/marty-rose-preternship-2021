#!/usr/bin/python3

# Will McComis
# wmccomis@nd.edu
#
# getdData.py
# Created: 20 April 2021
# Purpose: Handle the current server data and tell user which machines are open 

import os


def getData():

    cpudata = {}
    opencores = {0: 0, 1: 0, 2: 0, 3: 0}

    output = os.popen('mpstat -P ALL 1 1').readlines()

    for line in output[4:20]:
        cpudata[line.strip().split()[2]] = line.strip().split()[12]

    serverdata = {
        0 : (cpudata['0'], cpudata['1'], cpudata['2'], cpudata['3']),
        1 : (cpudata['4'], cpudata['5'], cpudata['6'], cpudata['7']), 
        2 : (cpudata['8'], cpudata['9'], cpudata['10'], cpudata['11']), 
        3 : (cpudata['12'], cpudata['13'], cpudata['14'], cpudata['15'])
        }

    for server in serverdata:
        for index, value in enumerate(serverdata[server]):
            if float(value) > 99:
                opencores[server] += 1

    return opencores