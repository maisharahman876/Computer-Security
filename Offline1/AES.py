
def gen_func(lst):
    n=int(len(lst)/4)
    r=0
    if n==4:
        r=10
    elif n==6:
        r=12
    elif n==8:
        r=14
    for i in range(0,r):
                
class AES:
    def __init__(self, key, size,padding):
        self.key=key
        self.size=int(size/8)
        #print({self.size})
        lst = list()
        
        for i in key:
            lst.append(hex(ord(i)))
        lst2= [int(x, 16) for x in lst]
        #print(lst2)
        ascii_string=''
        if len(lst)>self.size:
            lst2 = lst2[: self.size]
            # for i in lst2:
            #     ascii_string+=chr(i)
            # print(ascii_string)
        elif len(lst)<self.size:
            for i in range(len(lst),self.size):
                lst2.append(ord(padding))
        print(lst2)
        gen_func(lst2)
        if size==128:
            print("meo")
        elif size==192:
            print("meo")
        elif size==256:
            print("meo")
    def encrypt(self,msg):
        print("meo")
if __name__ == '__main__':
    aes=AES("Thats my Kung Fu",128,"*")