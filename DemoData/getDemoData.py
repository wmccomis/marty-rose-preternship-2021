#!/usr/bin/env python3
# get_data.py
# Author: Luis Sosa Manubes
# Date: April 16, 2020
# Program will create a json file with file mame, run-time, urgency and size. An sequential ID number will be created for each file
# For simulation purposes, urgency will be assigned randomly with a value from 1 (less urgent) to 10 (most urgent)

# run time will be measured in seconds, and recorded in a category from 1 (least time) to 5 (most time)
# Size is in bytes

import os, sys, random, time
# read all ls program and initialize values
ls=os.popen('ls')
ID_NUMBER=1
# open data.json, print initial {
fileOut = open('data.json', 'w')
print('{', file=fileOut)

# loop through files in directory
for program in ls:
    program=program.rstrip()
    #make sure the program is not recursively running itself or that it isn't trash output. Make sure it does not run 'hulk.py' and it does not run the cache directory some scripts may create
    if program != os.path.basename(sys.argv[0]) and program != 'data.json' and 'txt' not in program and program != "hulk.py" and program != "__pycache__":
        #redirect program call into &> to simulate stdout output
        prog_call=f'./{program} > /dev/null'
        print(f'now running: {prog_call}') 

        # measure run-time
        start_time=time.time()
        os.system(prog_call)
        program_time=time.time() - start_time
        # convert approximate run_time to 1-5
            # Parameteres
            # less than one second = 1
            # more than one second and less than one minute = 2
            # more than one minute, less than ten = 3
            # more than ten minutes, less than thirty = 4
            # more than thirty minutes = 5

        if program_time<1:
            program_time = 1
        elif program_time>=1 and program_time<60:
            program_time = 2
        elif program_time >= 60 and program_time < 600:
            program_time = 3
        elif program_time >= 600 and program_time < 3000:
            program_time = 4
        else:
            program_time = 5
        # get size 
        size_string=f"stat {program} | grep -E 'Size *' | cut -d ' ' -f 4"
        size=os.popen(size_string).read()
        size=size.rstrip()

        # obtain number of cores necessary for each file
        # obtain x_time function that will return a number between 0.2 and 1
        f_xtime=(0.2*program_time)

        #obtain a x_size function that will return a number between 0 and 1
        f_xsize=1-(1/( (float(size)/500)**2 + 1) )
        # get sum and estimate cores neeeded depending on estimated run time and size
        fx_sum=f_xtime+f_xsize
        if fx_sum<0.5:
            cores_estimation=1
        elif fx_sum>=0.5 and fx_sum<1:
            cores_estimation=2
        elif fx_sum >= 1 and fx_sum < 1.5:
            cores_estimation = 3
        else:
            cores_estimation = 4
        
        # add ID_NUMBER, run-time, urgency, size and number of cores needed
        json_output=f'''    "{ID_NUMBER}": {{
               "name": "{program}",
                "approximate_run_time": "{program_time}",
                "urgency": "{random.randint(1,10)}",
                "size": "{size}",
                "core_estimation": "{cores_estimation}"
                }},
        '''
        
        # update ID number
        ID_NUMBER+=1
        print(json_output, file=fileOut)

#manually add hulk.py
program="hulk.py"
size_string=f"stat {program} | grep -E 'Size *' | cut -d ' ' -f 4"
size=os.popen(size_string).read()
size=size.rstrip()

# add ID_NUMBER, run-time, urgency, size and number of cores needed
json_output=f'''   "{ID_NUMBER}": {{
          "name": "{program}",
          "approximate_run_time": "5",
          "urgency": "{random.randint(1,10)}",
          "size": "{size}",
          "core_estimation": "4"
        }},
    '''
            
print(json_output, file=fileOut)

# close file
print('}', file=fileOut)
fileOut.close()
print("File ready")
