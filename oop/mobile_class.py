class mobile:
    
    def __init__(self,name,price,dis,vat,):
        self.name=name 
        # --->>> another way to take input
        # self.brand="samsung"
        self.price=price
        self.dis=dis 
        self.vat=vat
        

    def work(self):
        d_amount = self.price * self.dis / 100

        price_after_dis = self.price - d_amount

        v_amount = self.price * self.vat / 100

        price_after_vat = price_after_dis + v_amount

        selling_price=price_after_vat
        print(f"The last selling price after discount and vat is {selling_price}")

    
galaxy=mobile('Samsung',25000,20,15,)
galaxy.work()



