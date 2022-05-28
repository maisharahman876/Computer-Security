from re import I
import socket            
import json
import AES
import RSA
from pathlib import Path
# Create a socket object
if __name__ == '__main__':
    fle = Path("Don’t Open this/DPT.txt")
    fle.touch()
    #k=[16,32,64,128]
    s = socket.socket()        
    port = 12345               
    s.connect(('127.0.0.1', port))
    
    data = s.recv(1024)
    data = json.loads(data.decode())
    cypher_txt = data.get("a")
    encrypted_key = data.get("b")
    n = data.get("c")
    size=data.get("d")
    #print(n)
    
    rsa=RSA.RSA(16)
    f = open("Don’t Open this/PVT.txt", "r")
    d=f.read()
    f.close()

    key=rsa.decrypt(encrypted_key,int(d),n)
    aes=AES.AES(key,size*8," ")
    PT=aes.decrypt(cypher_txt)
    f=open("Don’t Open this/DPT.txt",'w')
    f.seek(0)
    f.write("Key : ")
    f.write(key)
    f.write("\nPlain Text : ")
    f.write(PT)
    f.close()
    s.close()    
