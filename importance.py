#!/usr/bin/python3

# Luke Marushack
# Created: 24 April 2021
# Purpose: determine the importance of a given code segment.

def get_importance(run_time, urgency, estimated_cores):
    # Run Time: 1-5, 5 longest
    # Urgency: 1-10, 5 highest
    # Cores: 1-4, 4 highest
    # Most Importance = few cores, high urgency, low runtime. Those go first.
    rt_mult = 3
    urgency_mult = 3 
    cores_mult = 2

    importance = rt_mult*(6 - int(run_time)) + urgency_mult*int(urgency) + cores_mult * (5 - int(estimated_cores))
    return importance
