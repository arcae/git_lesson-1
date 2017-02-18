#!/usr/bin/python3

import urllib.request
from xml.etree.ElementTree import XML
import sys

if len(sys.argv) != 3:
  raise SystemExit('Usage:nextbus.py route stopid')

route = sys.argv[1]
stopid = sys.argv[2]

u = urllib.request.urlopen('http://ctabustracker.com/bustime/map/getStopPredictions.jsp?route={}&stop={}'.format(route,stopid))

data = u.read()
#print('Response:',data)

doc = XML(data)

import pdb; pdb.set_trace() #Launch debugger

for pt in doc.findall('.//pt'):
    print(pt.txt)


