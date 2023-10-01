 # class mobile:
#     def __init__(self , name , brand , price):
#         self.name = name 
#         self.price = price 
#         self.brand = brand
#     def detail(self):
#         print(f"The mobile name is {self.name} and brand is {self.brand} and price is {self.price}")

# class iphone(mobile):
#     def __init__(self,name, brand, price, cemra,ram):
#         super().__init__(name,brand,price)
#         self.cemra=cemra
#         self.ram=ram
#     def iphone_detail(self):
#         print(f"The mobile name is {self.name} and brand is {self.brand} and price is {self.price} and cemra name is {self.cemra} and ram is {self.ram}")

# class android(iphone):
#     def __init__(self, name, brand, price, cemra, ram,software,battery):
#         super().__init__(name, brand, price, cemra, ram)
#         self.software=software
#         self.battery=battery
#     def andr_detail(self):
#         print(f"The mobile name is {self.name} and brand is {self.brand} and price is {self.price} and cemra name is {self.cemra} and ram is {self.ram} and your software is {self.software} and battery is {self.battery} ")

# obj=android('samsung','galaxy',25000,'duos','4gb','adroid os' ,'5000mah')
# obj.detail()
# obj.iphone_detail()
# obj.andr_detail()
# obj2=iphone('iphone x','apple',150000,'50 mp','4gb')
# obj2.iphone_detail()



# class Area:
#     def __init__(self, l,b):
#         self.l=l
#         self.b=b
#     def show1(self):
#         print(f"your total area is {self.l*self.b}")
#     class Volume():
#         pass
#     class Rat(Volume):
#         pass
