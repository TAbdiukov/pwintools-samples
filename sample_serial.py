#!python2
# -*- coding: utf8 -*-

from pwintools import *

print("Opening  pipe...")
p = SerialTube(port="COM1")
print("Entering loop...")
while(True):
	buf = p.recvline()
	assert(len(buf))
	soup = buf.split(' ')
	s1 = soup[3]
	n1 = int(s1)
	n2 = n1 + 1
	s2 = str(n2)
	ans = "R!Received a number: "+s1+". x + 1 = "+s2
	print(ans)
	p.send(ans)
