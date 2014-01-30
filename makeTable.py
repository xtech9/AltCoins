#!/usr/bin/env python
"""
make markdown table from csv data
"""

from cryptsy import *

def get_data():
    """get as array"""
    with open('alts.csv','r') as f:
        lines = f.readlines()
        lines = [line.replace('\n','') for line in lines]
        arr = [line.split(';') for line in lines]
        return arr

def transform_data(data):
    """markdown beautify"""
    for d in data:
        url = d[2]
        if 'bitcointalk' in url:
            url = '[bitcointalk](' + url + ')'
        d[2] = url

    coins = cryptsy_coins()
    for d in data:
        if d[0] in coins.keys():
            print 'cryptsy'
            d[-2] = " X "
        else:
            d[-2] = ""

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
