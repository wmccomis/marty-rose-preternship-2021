#!/usr/bin/python3

# Luke Marushack
# lmarusha@nd.edu
#
# reciever.py
# Created: 10 May 2021
# Purpose: handle the input of a job and determine which machine to send it to

def handle_job(server_data, estimated_cores, prev_cores):
    # server_data is a dictionary, estimated_cores is an integer
    serverID = -1

    curr_core = (prev_cores + 1) % 4
    opencores = server_data[curr_core]

    if ((int) estimated_cores <= (int) opencores):
        serverID = curr_core
        cores_used = estimated_cores

    if (serverID == -1):
        print("That server is currently in use. Please wait...\n")
        return [-1, -1]

    print(f'\nThis job will be sent to the next server in the round-robin, server {serverID}, and will use {cores_used} cores.\n')
    return serverID, cores_used  

