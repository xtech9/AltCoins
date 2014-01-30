#!/usr/bin/env python
"""
make markdown table from csv data
"""

from cryptsy import *
from bter import *

def get_data():
    """get as array"""
    with open('alts.csv','r') as f:
        lines = f.readlines()
        lines = [line.replace('\n','') for line in lines]
        arr = [line.split(';') for line in lines]
        return arr

CCC = 0
NAME = 1
LINK = 2
LAUNCH = 3
TIER = 4
CRYP = 5
BTER = 6

def transform_data(data):
    """transform data 
    markdown beautify
    insert exchange data"""

    #for each exc
    for d in data:
        d += ['','']
        print len(d)

    for d in data:
        url = d[LINK]
        if 'bitcointalk' in url:
            url = '[bitcointalk](' + url + ')'
        d[LINK] = url

    cryptsy = cryptsy_coins()
    bter = bter_coins()

    for d in data:
        if d[0] in cryptsy.keys():
            print 'cryptsy'
            d[CRYP] = "X"
        else:
            d[CRYP] = ""

    for d in data:
        if d[0] in bter:
            print 'bter'
            d[BTER] = "X"
        else:
            d[BTER] = ""

    return data

def tier_write(f,data):
    #todo: pull from csv head
    head  = ['CCC','name','URL','launched','cryptsy listed','tier']
    
    headers = '|'.join(head)
    sep = ':---:|:---:|:---:|:---:|:---:|:---:'

    f.write('|' + headers + '|\n')
    f.write(sep + '\n')

    i = 1
    for row in data:
        line = '|'.join(row)
        f.write(line + '\n')

if __name__=='__main__':
    with open('alts.md','w') as f:
        f.write('# Alternative Cryptocurrencies\n')
        coins = get_data()
        coins = transform_data(coins)
        tiers = set([x[-1] for x in coins])
        tiers = sorted(tiers)
        for tier in tiers:
            print tier
            f.write('\n## ' + tier + '\n\n')
            tierdata = [x for x in coins if x[-1] == tier]
            tier_write(f,tierdata)
