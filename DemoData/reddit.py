#!/usr/bin/env python3

import os
import sys
import json
import requests
import re

# Constants

ISGD_URL = 'http://is.gd/create.php'

# Functions

def usage(status=0):
    ''' Display usage information and exit with specified status '''
    print('''Usage: {} [options] URL_OR_SUBREDDIT

    -s          Shorten URLs using (default: False)
    -n LIMIT    Number of articles to display (default: 10)
    -o ORDERBY  Field to sort articles by (default: score)
    -t TITLELEN Truncate title to specified length (default: 60)
    '''.format(os.path.basename(sys.argv[0])))
    sys.exit(status)

def load_reddit_data(url):
    ''' Load reddit data from specified URL into dictionary

    >>> len(load_reddit_data('https://reddit.com/r/nba/.json'))
    27

    >>> load_reddit_data('linux')[0]['data']['subreddit']
    'linux'
    '''
    # TODO: Verify url parameter (if it starts with http, then use it,
    # otherwise assume it is just a subreddit).
    URL=re.compile('https')
    if not URL.search(url):
        url='https://www.reddit.com/r/'+url+'/.json'

    return[url]

def shorten_url(url):
    ''' Shorten URL using is.gd service

    >>> shorten_url('https://reddit.com/r/aoe2')
    'https://is.gd/dL5bBZ'

    >>> shorten_url('https://cse.nd.edu')
    'https://is.gd/3gwUc8'
    '''
    # TODO: Make request to is.gd service to generate shortened url.
    return ''

def print_reddit_data(data, limit=10, orderby='score', titlelen=60, shorten=False):
    ''' Dump reddit data based on specified attributes '''
    # TODO: Sort articles stored in data list by the orderby key, and then
    # print out each article's index, title, score, and url using the following
    # format:
    #
    #   print(f'{index:4}.\t{title} (Score: {score})\n\t{url}')
    #
    # Note: Trim or modify the output based on the keyword arguments to the function.

    # fetching the data
    headers={'user-agent': 'reddit-{}'.format(os.environ.get('USER', 'cse-20289-sp21'))}
    r=requests.get(url, headers=headers)
    r.raise_for_status()
    redditData=json.loads(r.text)
    
    # sorting order
    if orderby=='score':
        rev=True
    else:
        rev=False

    redditData=sorted(redditData, key, reverse=rev)


def main():
    # TODO: Parse command line arguments
    arguments = sys.argv[1:]
    url       = None
    limit     = 10
    orderby   = 'score'
    titlelen  = 60
    shorten   = False

    # TODO: Load data from url and then print the data

    for arg in arguments[1:-2]:
        if arg=='-s':
            shorten=True
        if arg=='-n':
            limit=(arg+1)
        if arg=='-o':
            orderby=not_score
        if arg=='-t':
            titlelen=arg+1
        else:
            usage(1)

    if shorten:
        shorten_url(url)
    
# Main Execution

if __name__ == '__main__':
    main()

# vim: set sts=4 sw=4 ts=8 expandtab ft=python: