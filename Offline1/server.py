import socket            
def AES_Encrypt(msg,key):
    print(msg)


if __name__ == '__main__':
# next create a socket object
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
        while True:
            c.send('Thank you for connecting'.encode())
        c.close()
        break