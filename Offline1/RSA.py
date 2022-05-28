import sympy
import math
import time
def gcd(a, b) :
     
    if (a == 0) :
        return b
         
    return gcd(b % a, a)
class RSA:
    def __init__(self, k):
        self.k=k
    def key_generation(self):
        key_len=int(self.k/2)
        min=2
        max=math.pow(2,key_len)
       
        p = sympy.randprime(min, max)
        q = sympy.randprime(min, max)
        while p==q:
            p = sympy.randprime(min, max)
            q = sympy.randprime(min, max)
        self.n=p*q
        self.phi=(p-1)*(q-1)
        self.e=1
        for i in (2,self.phi):
            if gcd(i,self.phi)==1:
                self.e=i
                break
        # i=1
        # while True:
        #     self.d=(self.phi*i+1)/self.e
        #     if self.d.is_integer():
        #         self.d=int(self.d)
        #         break
        #     i+=1
        i = 1
        self.d=1
        while (((self.phi*i)+1) % self.e) != 0:
            i = i+1
        self.d = int(((self.phi*i)+1) // self.e)
        return self.d,self.n
    def encrypt(self,msg):
        lst=list()
        encrypt=list()
        for m in msg:
            lst.append(hex(ord(m)))
        chars= [int(x, 16) for x in lst]
        for i in chars:
            encrypt.append(pow(i,self.e,self.n))
        return encrypt
    def decrypt(self,lst,d,n):
        data=list()
        for i in lst:
            data.append(pow(i,d,n))
        string=''
        for i in data:
            string+=chr(i)
        return string




if __name__ == '__main__':
    k=[16,32,64,128]
    
    print("Enter your Message: ")
    msg=input()
    for i in k:
       
        rsa=RSA(i)
        st=time.time()
        d,n=rsa.key_generation()
        end=time.time()
        key_gen=end-st
    
        st=time.time()
        lst=rsa.encrypt(msg)
        end=time.time()
        plain=rsa.decrypt(lst,d,n)
        end1=time.time()

    

        print("\nExecution Time for k ==",i)
        print("Key Scheduling : ",key_gen," seconds")
        print("Encryption Time : ",end-st," seconds")
        print("Encryption Time : ",end1-end," seconds")
    
    
   