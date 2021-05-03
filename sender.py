#!/usr/bin/python3

# Will McComis
# wmccomis@nd.edu
#
# sender.py
# Created: 20 April 2021
# Purpose: Handle the input and send the file to the correct server 

import os
from getData import *
import random


# Function takes in jobData and server choice and run the job on the correct cores from the desired server based up capacity

def sender(jobData):
    opencores = []

    for index, core in enumerate(getData()[jobData["Server"]]):
        if float(core) > 99:
            opencores.append(4*jobData["Server"] + index)
            
    if len(opencores) == jobData["Cores"]:
        cores = ''.join(str(opencores)[1:-1].split())

    elif len(opencores) > jobData["Cores"]:
        randlist = random.sample(opencores, jobData["Cores"])
        cores = ''.join(str(randlist)[1:-1].split())

    else: 
        cores = ''.join(str(opencores)[1:-1].split())

    # runs the command on the cores, sends output to a text file, and runs file in background
    
    os.system(f"sudo chrt -r 1 taskset -c {cores} ./DemoData/{jobData['Command']} > {jobData['Command'].txt &")



# SAMPLE FUNCTION CALL:

# job = {"Command" : "hulk.py -l 5 -c 6", "Cores" : 4, "Server" : 2}
# sender(job)
