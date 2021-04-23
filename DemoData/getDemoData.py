#!/usr/bin/env python3
# get_data.py
# Author: Luis Sosa Manubes
# Date: April 16, 2020
# Program will create a json file with file mame, run-time, urgency and size. An sequential ID number will be created for each file
# For simulation purposes, urgency will be assigned randomly with a value from 1 (less urgent) to 10 (most urgent)

# Data will be displayed in seconds
# Size is in kylobytes

import os, sys, random, time
# read all ls program and initialize values
ls=os.popen('ls')
ID_NUMBER=0
# open data.json, print initial {
fileOut = open('data.json', 'w')
print('{', file=fileOut)


# loop through files in directory
for program in ls:
    program=program.rstrip()
    #make sure the program is not recursively running itself or that it isn't trash output
    if program != os.path.basename(sys.argv[0]) and program != 'data.json' and 'txt' not in program:
        #redirect program call into &> to simulate stdout output
        prog_call=f'./{program} > {program}.txt'
    
        # measure run-time
        start_time=time.time()
        os.system(prog_call)
        program_time=time.time() - start_time

        # update ID number
        ID_NUMBER+=1

        # get size 
        size_string=f"stat {program} | grep -E 'Size *' | cut -d ' ' -f 4"
        size=os.popen(size_string).read()
        size=int(size.rstrip())

        ## TODO obtain number of cores necessary for each file

        # add ID_NUMBER, run-time, urgency, size and number of cores needed
        json_output=f'''"{ID_NUMBER}": [
            name: {program},
            approximate_run_time: {program_time},
            urgency: {random.randint(1,10)},
            size: {size}
            ],
        '''
        

        print(json_output, file=fileOut)
        # clear screen
        os.system('clear')

#TODO: manually run hulk.py with 6 cores

print('}', file=fileOut)
fileOut.close()
