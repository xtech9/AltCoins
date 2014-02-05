"""
"""

def bter_coins():
     coins = list()
     with open('bter.csv','r') as f:
          lines = f.read()
          for z in lines.split(','):
               if '_' in z:
                    x = z.split(':')[0]
                    x = x.replace('"','')
                    if 'vol' in x: continue
                    if not 'btc' in x: continue
                    x = x.split('_')[0]
                    x = x.upper()
                    coins.append(x)
     return coins[1:]

