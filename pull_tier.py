import urllib2

u = urllib2.urlopen('https://raw2.github.com/benjyz/AltCoins/gh-pages/alts.csv')
s = u.read()
altcoins = s.split('\n')[1:]
print '*'*20
print 'tier2'
for altcoin in altcoins:
    arr = altcoin.split(';')
    if arr[-1] == 'tier2':
        print altcoin

"""
********************
tier2
DOGE;Dogecoin;https://bitcointalk.org/index.php?topic=361813.0;8/12/2013;tier2
MSC;mastercoin;https://bitcointalk.org/index.php?topic=265488.0;9/1/2013;tier2
NMC;Namecoin;http://namecoin.info/;4/11/2011;tier2
QRK;Quark;https://bitcointalk.org/index.php?topic=260031.0;;tier2
PTS;ProtoShares;https://bitcointalk.org/index.php?topic=325261.0;;tier2
WDC;Worldcoin;https://bitcointalk.org/index.php?topic=204894.0;;tier2
MEC;Megacoin;https://bitcointalk.org/index.php?topic=218851.0;;tier2
XPM;PrimeCoin;https://bitcointalk.org/index.php?topic=251850.0;;tier2
IFC;infinitecoin;https://bitcointalk.org/index.php?topic=225891.0;;tier2
FTC;FeatherCoin;https://bitcointalk.org/index.php?topic=178286.0;;tier2
NVC;NovaCoin;https://bitcointalk.org/index.php?topic=143221.0;;tier2
TIX;Tickets;https://bitcointalk.org/index.php?topic=297666.0;;tier2
DVC;Devcoin;https://bitcointalk.org/index.php?topic=34586.0;;tier2
ZET;Zetacoin;https://bitcointalk.org/index.php?topic=267545.0;;tier2
TRC;Terracoin;http://terracoin.org/;;tier2
DGC;DigitalCoin;https://bitcointalk.org/index.php?topic=209508.0;;tier2
ANC;Anoncoin;https://bitcointalk.org/index.php?topic=227287.0;;tier2
FRC;Freicoin;http://www.freicoin.org/;;tier2
"""
