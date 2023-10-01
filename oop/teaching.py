# class tiktok:
#     def __init__(self,l,c):
#         self.l=l
#         self.c=c
#     def tinfo(self):
#         print(f"Details of Tiktok is ")
#         print(f"your like is {self.l} and comment is {self.c} \n ")

# class youtube(tiktok):
#     def __init__(self,l,c,v,s):
#         super(). __init__(l,c)
#         self.v=v
#         self.s=s
#     def info(self):
#         print(f"Details of youtube is ")
#         print(f"your like is {self.l} comment is {self.c} view is {self.v} and subscriber is {self.s}")

# obj=youtube(1,2,3,4)
# obj.tinfo()
# obj.info()

# obj=tiktok(8,9)
# obj.tinfo()

class A:
    def __init__(self,price,dis,sp):
        self.price=price
        self.dis=dis
        self.sp=sp
    def ainfo(self):
        self.sp=self.price-self.dis
        print(f"The selling price is {self.sp}")

class B(A):
    def __init__(self, price, dis,vat,rprice):
        super().__init__(price, dis,)
        self.vat=vat
        self.rprice=rprice
        self.rprice=self.sp+self.vat
    def binfo(self):
        print(f"The selling price after vat is {self.rprice}")
obj=B(12000,120,90,0)
obj.ainfo()
obj.binfo()