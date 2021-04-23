#!/usr/bin/env python3

import collections
import os
import sys

import requests

# Constants

URL     = 'https://yld.me/raw/bWhu'
TAB     = ' '*8
GENDERS = ('M', 'F')
ETHNICS = ('B', 'C', 'N', 'O', 'S', 'T', 'U')

# Functions

def usage(status=0):
    ''' Display usage information and exit with specified status '''
    progname = os.path.basename(sys.argv[0])
    print(f'''Usage: {progname} [options] [URL]

    -y  YEARS   Which years to display (default: all)
    -p          Display data as percentages.
    -G          Do not include gender information.
    -E          Do not include ethnic information.
    ''')
    sys.exit(status)

def load_demo_data(url=URL):
    ''' Load demographics from specified URL into dictionary

    >>> load_demo_data('https://yld.me/raw/ilG').keys()
    dict_keys(['2013', '2014', '2015', '2016', '2017', '2018', '2019'])

    >>> load_demo_data('https://yld.me/raw/ilG')['2013'] == \
            {'M': 1, 'B': 2, 'F': 1, 'TOTAL': 2}
    True

    >>> load_demo_data('https://yld.me/raw/ilG')['2019'] == \
            {'M': 1, 'U': 2, 'F': 1, 'TOTAL': 2}
    True
    '''
    # TODO: Request data from url and load it into dictionary organized in the
    # following fashion:
    #
    #   {'year': {'gender': count, 'ethnic': count, 'TOTAL': count}}
    req=requests.get(url)
    data=req.text

    dict={}
    temp={}
    data=data.split('\n')[1:-1]

    for line in data:
        line=line.split(',')

        if line[0] in dict:
            temp[line[0]]+=1
        else:
            dict[line[0]]={}
            temp[line[0]]=1

        if line[1] in dict[line[0]].keys():
            dict[line[0]][line[1]]+=1
        else:
            dict[line[0]][line[1]] =1

        if line[2] in dict[line[0]].keys():
            dict[line[0]][line[2]]+=1
        else:
            dict[line[0]][line[2]]=1

    for year in temp:
        dict[year]['TOTAL']=temp[year]

    return dict

def print_demo_separator(years, char='='):
    ''' Print demographics separator

    Note: The row consists of the 8 chars for each item in years + 1.

    >>> print_demo_separator(['2012', '2013'])
    ========================
    '''
    # TODO: Print row of separator characters
    print(f"{char}"*(8*(len(years)+1)))

def print_demo_years(years):
    ''' Print demographics years row

    Note: The row is prefixed by 4 spaces and each year is right aligned to 8
    spaces ({:>8}).

    >>> print_demo_years(['2012', '2013'])
            2012    2013
    '''
    # TODO: Print row of years
    print( " " * 4, end="")
    for year in years:
        print(f"{year:>8}", end="")


def print_demo_fields(data, years, fields, percent=False):
    ''' Print demographics information (for particular fields)

    Note: The first column should be a 4-spaced field name ({:>4}), followed by
    8-spaced right aligned data columns ({:>8}).  If `percent` is True, then
    display a percentage ({:>7.1f}%) rather than the raw count.

    >>> data  = load_demo_data('https://yld.me/raw/ilG')
    >>> years = sorted(data.keys())
    >>> print_demo_fields(data, years, GENDERS, False)
       M       1       1       1       1       1       1       1
       F       1       1       1       1       1       1       1
    '''
    # TODO: For each field, print out a row consisting of data from each year.
    for row in fields:
        print(f"{row:>4}", end="")
        for i in years:
            if percent:
                print("{:>7.1f}%".format(data[i].get(row,0)/data[i].get("TOTAL")*100),end="")
            else:
                print("{:>8}".format(data[i].get(row, 0)), end="")
        print()

def print_demo_data(data, years=None, percent=False, gender=True, ethnic=True):
    ''' Print demographics data for the specified years and attributes '''
    if years== None:
        years=list(data.keys())
    else:
        years=years.split(',')

    years=sorted(years)
    print_demo_years(years)
    
    tempL = sorted(list(data.keys()))
    tempD = {}

    for i in tempL:
        if i not in tempD:
            tempD[i] = {}
        for g in GENDERS:
            if g in data[i]:
                tempD[i][g] = data[i][g]
        for e in ETHNICS:
            if e in data[i]:
                tempD[i][e]=data[i][e]
        tempD[i]["TOTAL"] = data[i]["TOTAL"]
    
    sortD=tempD
    print()
    print_demo_separator(years, '=')

    if gender:
        print_demo_gender(sortD, years, percent)

    if ethnic:
        print_demo_ethnic(sortD, years, percent)

def print_demo_gender(data, years, percent=False):
    ''' Print demographics gender information '''
    print_demo_fields(data, years, GENDERS, percent)
    print_demo_separator(years, '-')

def print_demo_ethnic(data, years, percent=False):
    ''' Print demographics ethnic information '''
    print_demo_fields(data, years, ETHNICS, percent)
    print_demo_separator(years, '-')

def main():
    ''' Parse command line arguments, load data from url, and then print
    demographic data. '''
    # TODO: Parse command line arguments
    arguments = sys.argv[1:]
    url       = URL
    years     = None
    gender    = True
    ethnic    = True
    percent   = False

    # TODO: Load data from url and then print demograpic data with specified
    # arguments
    for index, arg in enumerate(arguments):
        if arg=='-h':
            usage(0)
        elif arg=='-y':
            years=arguments[index+1]
        elif arg=='-p':
            percent= True
        elif arg == '-G':
            gender = False
        elif arg == '-E':
            ethnic = False
        elif 'https' in arg:
            url=arg
        elif arg.startswith("-"):
            usage(1)
    print_demo_data(load_demo_data(url), years, percent, gender, ethnic)

# Main Execution

if __name__ == '__main__':
    main()

# vim: set sts=4 sw=4 ts=8 expandtab ft=python:
