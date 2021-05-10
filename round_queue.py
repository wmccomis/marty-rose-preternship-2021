#!/usr/bin/python3

# Luke Marushack
# Created: 10 May 2021
# Purpose: handle all of the input jobs and process them into a queue. 

from queue import Queue
from time import sleep
import json

from round_robin import *
from importance import *
from sender import *

def format_task(name, cores, server):
    return  {"Command" : name, "Cores" : cores, "Server" : server}

def process_jobs(filename):
    q = Queue()

    data = json.load(open(filename, "r"))
    for key in data.keys():
        data[key]["importance"] = get_importance(data[key]["approximate_run_time"], data[key]["urgency"], data[key]["core_estimation"])

    for item in data.keys():
        q.put(data[item])

    serverID = 0
    while (not q.empty()):
        curr_job = q.queue[0]
        serverID, cores_used = handle_job(summedData(), curr_job["core_estimation"], serverID)
        if (serverID == -1):
            sleep(0.5)
            continue
        jobdata = format_task(curr_job["name"], cores_used, serverID)
        print(jobdata)
        sender(jobdata)
        q.get()

process_jobs("data.json")
