
#get launch dates

import urllib2

def get_data():
    """get as array"""
    with open('alts.csv','r') as f:
        lines = f.readlines()
        lines = [line.replace('\n','') for line in lines]
        arr = [line.split(';') for line in lines]
        return arr

def first_date(link):
    try:
        u = urllib2.urlopen(link)
        s = u.read()
        i = s.index('td_headerandpost')
        s = s[i:]
        j = s.index('<div class="smalltext">')
        s = s[j+10:j+160]
        #s = s.split('>')[1]
        #s = s.split('<')[0]
        #s = s.split(',')[:-1]
        x = 'class="edited"' in s

        if x:
            i = s.index('class="edited"')
            s = s[i:]
            s = s.split('<')[0]
            s = ''.join(s.split('>')[1:])
            #ignore time
            i = s.index(':')
            s = s[:i-4]
            print s
            return s
        else:
            return ""
    except:
        return ""

data = get_data()
with open('launchdates.csv','w') as f:
    for d in data[:]:
        l = d[2]
        print l
        ldate = first_date(l)
        f.write(d[0] + ';' + ldate + '\n')
