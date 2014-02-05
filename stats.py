"""
alt coin market statistics
"""

import urllib2

turl ="https://raw.github.com/benjyz/AltCoins/master/alts.csv"
u = urllib2.urlopen(turl)
s = u.read()

data = s.split('\n')
data = [x.split(';') for x in data]
allt = [x[-1] for x in data]
tiers = sorted(set(allt))
for tier in tiers:
    print tier,allt.count(tier)

print 'all : ',len(allt)


