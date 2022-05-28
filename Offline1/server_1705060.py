import socket            
import AES
import RSA
import json
import os
from pathlib import Path

if __name__ == '__main__':
    #k=[16,32,64,128]
# next create a socket object
    print("Enter key Size of RSA(16/32/64/128) : ")
    rsa_s=int(input())
    print("Enter key Size of AES(16/24/32) : ")
    aes_s=int(input())
    print("Enter your AES key : ")
    key=input()
    aes=AES.AES(key,aes_s*8," ")
    print("Enter your Message: ")
    msg=input()
    cypher_txt=aes.encrypt(msg)
    CT=list()
    for i in cypher_txt:
        CT.append(int(i))

    s = socket.socket()        
    print ("Socket successfully created")
    port = 12345               
    s.bind(('', port))        
    print ("socket binded to %s" %(port))
    s.listen(5)    
    print ("socket is listening")           
    while True:
        c, addr = s.accept()    
        print ('Got connection from', addr )
        # print("Enter key Size of RSA(16/32/64/128) : ")
        # rsa_s=int(input())
        
        #c.send(aes_s)
        
        if not os.path.exists("Don’t Open this/"):
            os.makedirs("Don’t Open this/",mode=0o777, exist_ok=False)
        
        fle = Path("Don’t Open this/PVT.txt")
        fle.touch(exist_ok=True)
        rsa=RSA.RSA(rsa_s)
        d,n=rsa.key_generation()
        f=open("Don’t Open this/PVT.txt",'w')
        f.write(str(d))
        f.close()
        
        encrypted_key=rsa.encrypt(key)
        # print(type(cypher_txt))
        # print(len(encrypted_key))
        data = json.dumps({"a":CT,"b":encrypted_key, "c": n,"d":aes_s})
        c.send(data.encode())


        c.close()
        break