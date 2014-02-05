"""
transform alt data
"""
def get_data():
    with open('alts.csv','r') as f:
        lines = f.readlines()
        return lines

lines = get_data()
with open('alts2.csv','w') as f:
    i = 1
    for line in lines[1:]:
        line = line.replace('\n','')
        line = line.replace(' ','')
        arr = line.split('|')[1:-1]
        name,link = arr[1].split(']')
        link = link.replace('(','')
        link = link.replace(')','')
        name = name.replace('[','')
        name = name.replace(']','')
        arr = [arr[0],name,link]+arr[2:]
        tier = 'tier1'
        if i>=5 and i <=22:
            tier = 'tier2'
        elif i>=23 and i<=128:
            tier = 'tier3'
        elif i>=129 and i<=137:
            tier = 'tier5'
        elif i>=138:
            tier = 'tier6'
            
        arr.append(tier)
        s = ';'.join(arr)
        f.write(s + '\n')
        i+=1
