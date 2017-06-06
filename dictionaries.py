from urllib import urlopen

__author__ = 'Administrator'

def google_dict():
    gd = ['google', 'search for', 'search', 'look for', 'look', 'knowledge']
    return gd

import google

def unknown(text):
    x,y=[],[]
    gs=google.search('https://google.com/#q='+str(text),pause=2.0,stop=20)
    for link in gs:
        x.append(link)

    for i in x:
        y.append(i.split('/')[2])

    dictionary = dict(zip(x,y))
    return dictionary

unknown("hello world")
