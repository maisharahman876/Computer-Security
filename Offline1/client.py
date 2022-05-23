import socket            
 
# Create a socket object
if __name__ == '__main__':
    s = socket.socket()        
    port = 12345               
    s.connect(('127.0.0.1', port))
    while True:
        print (s.recv(1024).decode())
    s.close()    
