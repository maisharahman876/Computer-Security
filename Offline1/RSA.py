import sympy
import math
def gcd(a, b) :
     
    if (a == 0) :
        return b
         
    return gcd(b % a, a)
class RSA:
    def __init__(self, k):
        key_len=k/2
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
        i=1
        while True:
            self.d=(self.phi*i+1)/self.e
            if self.d.is_integer():
                self.d=int(self.d)
                break
            i+=1
    def encrypt(self,msg):
        
        



if __name__ == '__main__':
    rsa=RSA(16)