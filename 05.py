import urllib
import pickle

url = 'http://www.pythonchallenge.com/pc/def/banner.p'
resp = urllib.urlopen(url)
p = pickle.load(resp)

resp.close()

for i in p:
    a = [j[0] * j[1] for j in i]
    print ''.join(a)