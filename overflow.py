#!/usr/bin/python3

# Luke Marushack
# Created: 21 April 2021
# Purpose: handle all of the input jobs and process them into a queue. 

from queue import Queue
from time import sleep

def format_task(name, cores, server):
    return  {"Command" : name, "Cores" : cores, "Server" : server}

def process_jobs():
    q = Queue()
    """
    Still need Luis' core estimation code and the code that tells this program
    what jobs are about to be run. Then I can finish this script. 
    """
    while (not q.empty()):
        job = q.front()
        est_cores = estimated_cores(job)
        serverID, cores_used = handle_job(summedData(), est_cores)
        if (serverID == -1):
            sleep(0.5)
            continue
        jobdata = format_task(job[name], cores_used, serverID)
        sender(jobdata, serverID)
        q.pop()
