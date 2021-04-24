from queue import queue

def format_task(name, cores, server):
    return  {"Command" : name, "Cores" : cores, "Server" : server}

def process_jobs():
    q = queue
    """
    Still need Luis' core estimation code and the code that tells this program
    what jobs are about to be run. Then I can finish this script. 
    """
    while (not q.empty()):
        """
        JOB = q.pop()
        luis_estimated_cores(job)
        server, cores = handle_job(summedData(), cores)
        jobdata = format_task(server, cores) # dict(command:hulk.py -c 5, Cores:3)
        sender(jobdata, server)
        """


