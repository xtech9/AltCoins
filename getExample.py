"""
simple example for grepping a list of coins
"""

import urllib2

turl ="https://raw.github.com/benjyz/AltCoins/master/alts.csv"
u = urllib2.urlopen(turl)
s = u.read()

data = s.split('\n')
data = [x.split(';') for x in data]

tier1 = [x for x in data if x[-1] == 'tier2']
for coin in tier1:
    print '+ ' + ' '.join(coin)



