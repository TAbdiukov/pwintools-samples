#!python2

from pwintools import *

print("Opening  tube...")
p = SerialTube(port="COM4")
print("Entering loop...")
while(1):
	buf = p.recvline()
	assert(len(buf))
	soup = buf.split(' ')
	s1 = soup[3]
	n1 = int(s1)
	n2 = n1 + 1
	s2 = str(n2)
	ans = "R!Recv num: "+s1+". x + 1 = "+s2
	print(ans)
	p.send(ans)
