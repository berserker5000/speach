from urllib import urlopen

__author__ = 'Administrator'

def google_dict():
    gd = ['google', 'search for', 'search', 'look for', 'look', 'knowledge']
    return gd


from google import search
x = []
for i in search("hello world", stop=15):
    l = i.encode('ascii', 'ignore')
    x.append(l)

for i in x:
    print(i)