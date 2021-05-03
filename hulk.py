#!/usr/bin/python3

import concurrent.futures
import hashlib
import os
import string
import sys
import pprint

# Constants

ALPHABET = string.ascii_lowercase + string.digits

# Functions

def usage(exit_code=0):
    progname = os.path.basename(sys.argv[0])
    print(f'''Usage: {progname} [-a ALPHABET -c CORES -l LENGTH -p PATH -s HASHES]
    -a ALPHABET Alphabet to use in permutations
    -c CORES    CPU Cores to use
    -l LENGTH   Length of permutations
    -p PREFIX   Prefix for all permutations
    -s HASHES   Path of hashes file''')
    sys.exit(exit_code)

def md5sum(s):
    ''' Compute md5 digest for given string. '''
    # TODO: Use the hashlib library to produce the md5 hex digest of the given
    # string.
    s = hashlib.md5(s.encode())
    return s.hexdigest()

def permutations(length, alphabet=ALPHABET):
    ''' Recursively yield all permutations of alphabet up to given length. '''
    # TODO: Use yield to create a generator function that recursively produces
    # all the permutations of the given alphabet up to the provided length.
    if length==1:
        for i in alphabet:
            yield i
    else:
        for i1 in alphabet:
            for i2 in permutations(length-1, alphabet):
                yield i1+i2

def flatten(sequence):
    ''' Flatten sequence of iterators. '''
    # TODO: Iterate through sequence and yield from each iterator in sequence.
    for item in sequence:
        for item2 in item:
            yield item2

def crack(hashes, length, alphabet=ALPHABET, prefix=''):
    ''' Return all password permutations of specified length that are in hashes
    by sequentially trying all permutations. '''
    # TODO: Return list comprehension that iterates over a sequence of
    # candidate permutations and checks if the md5sum of each candidate is in
    # hashes.
    return [prefix + perm for perm in permutations(length, alphabet) if md5sum(prefix+perm) in hashes]

def whack(arguments):
    ''' Call the crack function with the specified list of arguments '''
    return crack(arguments[0], arguments[1], arguments[2], arguments[3])

def smash(hashes, length, alphabet=ALPHABET, prefix='', cores=1):
    ''' Return all password permutations of specified length that are in hashes
    by concurrently subsets of permutations concurrently.
    '''
    # TODO: Create generator expression with arguments to pass to whack and
    # then use ProcessPoolExecutor to apply whack to all items in expression.
    arguments=((hashes, length -1, alphabet, prefix + letter) for letter in alphabet)
    with concurrent.futures.ProcessPoolExecutor(cores) as executor:
        return flatten(executor.map(whack, arguments))

def main():
    arguments   = sys.argv[1:]
    alphabet    = ALPHABET
    cores       = 1
    hashes_path = 'hashes.txt'
    length      = 1
    prefix      = ''

    # TODO: Parse command line arguments
    for index, arg in enumerate(arguments):
        if arg== '-a':
            alphabet=arguments[index+1]
        elif arg=='-h':
            usage(1)
        elif arg=='-c':
            cores = int(arguments[index+1])
        elif arg=='-l':
            length=int(arguments[index+1])
        elif arg=='-p':
            prefix=arguments[index+1]
        elif arg=='-s':
            hashes_path=arguments[index+1]

    # TODO: Load hashes set
    temp=open(hashes_path).read()
    hashes=set(temp.split())

    # TODO: Execute crack or smash function
    if cores==1 or length==1:
        passwords = crack(hashes,length, alphabet, prefix)
    else:
        passwords = smash(hashes, length, alphabet, prefix, cores)

    # TODO: Print all found passwords
    for i in passwords:
        print(i)

# Main Execution

if __name__ == '__main__':
    main()

# vim: set sts=4 sw=4 ts=8 expandtab ft=python:
