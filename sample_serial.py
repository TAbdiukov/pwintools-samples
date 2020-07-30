#python2

"""
Simple test program for "pwintools"
How to:
1. download & install "com0com",
2. configure it to emulate one serial ports pair (eg COM3<-->COM4)
3. download & install "COM Port Data Emulator", set it up to
    * Use one of two ports (eg COM3)
    * (by default) Generate: random text
    ! Start (bottom right corner)
4. Run this text script
"""

from pwintools import *

p = serialtube(port="COM4")
print("Entering loop...")
while(1):
    buf = p.recvline()
    assert(len(buf))
    soup = buf.split(' ')
    s1 = soup[3]
    n1 = int(s1)
    n2 = n1 + 1
    s2 = str(n2)
    ans = "Recv number: "+s1+". This + 1 = "+s2
    print(ans)
    p.send_raw(ans)