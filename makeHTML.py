#!/usr/bin/env python
"""
make static html site
"""

from cryptsy import *
from bter import *



def get_launch():
     coins = dict()
     with open('launchdates.csv','r') as f:
          lines = f.readlines()
          for line in lines:
               line = line.replace('\n','')
               arr = line.split(';')
               coins[arr[0]] = arr[1]
     return coins

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

#messy hack
CRYP = 5
BTER = 6

def transform_data(data):
    """transform data
markdown beautify
insert exchange data"""

    #for each exc add a column
    newd = list()
    for d in data:
        d += ['-','-']
        newd.append(d)
    data = newd
        
    for d in data:
        #print len(d)
        link = d[LINK]
        if 'bitcointalk' in link:
            link = '<a href="' + link + '">bitcointalk</a>'
        else:
            link = '<a href="' + link + '">' + link + '</a>'
        d[LINK] = link

    cryptsy = cryptsy_coins()
    bter = bter_coins()
    launch = get_launch()

    for d in data:
        if d[0] in launch.keys():
            ld = launch[d[0]]
            d[LAUNCH] = ld

    for d in data:
        if d[0] in cryptsy.keys():
            d[CRYP] = "X"
        else:
            d[CRYP] = ""

    for d in data:
        if d[0] in bter:
            d[BTER] = "X"
        else:
            d[BTER] = ""

    return data

def ignore_col(data,col):
    newd = list()
    for d in data:
        newrow = d[:col] + d[col+1:]
        newd.append(newrow)
    return newd
        

def tier_write(f,data):
    #todo: pull from csv head
    head = ['CCC','name','URL','launched','cryptsy listing','bter listing']
    s = "<table><tr>"
    for h in head:
        s +="<th>" + h + "</th>"
    s += "</tr>"

    f.write(s)
    s = ""
    i = 1
    data = ignore_col(data,4)
    for row in data:
        r = "<tr>"
        for el in row:
            r+="<td>" + el + "</td>"
        r +="</tr>"
        f.write(r + '\n')

    s +="</table>"
    f.write(s)

if __name__=='__main__':
    with open('alts.html','w') as f:
        f.write('<h1>Alternative Cryptocurrencies</h1>\n')
        coins = get_data()
        tiers = set([x[TIER] for x in coins])
        coins = transform_data(coins)
        tiers = sorted(tiers)
        for tier in tiers:
            print tier
            f.write('<h2>' + tier + '</h2>\n')
            tierdata = [x for x in coins if x[TIER] == tier]
            tier_write(f,tierdata)
