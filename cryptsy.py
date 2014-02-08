"""
"""

def cryptsy_coins():
     coins = dict()
     with open('cryptsy.csv','r') as f:
          lines = f.readlines()
          for line in lines:
               arr = line.split(';')
               pair = arr[0]
               cur = pair.split('/')[0]
               coins[cur] = arr[1]
     return coins

#coins = get_coins()
#print coins
