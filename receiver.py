# Luke Marushack
# lmarusha@nd.edu
#
# reciever.py
# Created: 18 May 2021
# Purpose: handle the input of a job and determine which machine to send it to

def handle_job(server_data, estimated_cores):
    # server_data is a dictionary, estimated_cores is an integer
    serverID = ''
    cores_used = 10000 # arbitrarily large number

    # Code to get the server that has the number of cores closest to the estimated
    # number of cores needed for this code.
    for server, opencores in server_data.items():
        if (abs(opencores - estimated_cores) < abs(estimated_cores - cores_used)):
            serverID = server
            cores_used = min(open_cores, estimated_cores)
    if (serverID == ''):
        print("All servers are using all of their cores. Please wait until cores are available.\n")
        return [-1, -1]

    print(f'\nThis job will be sent to the server with the most available processing power, server {serverID}, and will use {cores_used} cores.\n')
    return [serverID, cores_used]  

# Validation Testing
"""
sd = [[1, 45], [2, 43], [3, 70], [4, 15]]
sd2 = [[1, 100],[2, 100],[3, 101]]
print(handle_job(sd))
print(handle_job(sd2))
"""

