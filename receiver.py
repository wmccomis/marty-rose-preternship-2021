# Luke Marushack
# lmarusha@nd.edu
#
# reciever.py
# Created: 18 May 2021
# Purpose: handle the input of a job and determine which machine to send it to

def handle_job(server_data):
    serverID = ''
    dest_usage = 100
    # Assume that data comes into server in the form of an array of arrays with data in the form of:
    # [serverID, current usage percent (out of 100)] 
    for num in range(len(server_data)):
        if (server_data[num][1] < dest_usage):
            serverID = server_data[num][0]
            dest_usage = server_data[num][1]
    if (serverID == ''):
        print("\nAll current servers are at maximum capacity. We will wait until one of the servers finishes a task.\n")
        return 0

    print(f'\nThis job will be sent to the server with the most available processing power, server {serverID}, currently at {dest_usage}% CPU usage.\n')
    return serverID  

# Validation Testing
"""
sd = [[1, 45], [2, 43], [3, 70], [4, 15]]
sd2 = [[1, 100],[2, 100],[3, 101]]
print(handle_job(sd))
print(handle_job(sd2))
"""

