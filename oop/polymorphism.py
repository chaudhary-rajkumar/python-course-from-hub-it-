class Vehicle:
    def __init__(self,name,color,price):
        self.name =name
        self.color =color
        self.price =price
    
    def show(self):
        print(f"Details are : {self.name} {self.color} {self.price}")
    def max_speed(self):
        print('Vehicle max speed is 150')
    def change_gear(self):
        print('Vehicle change 6 gear')

class Car(Vehicle):
    def max_speed(self):
        print('Vehicle max speed is 240')
    def change_gear(self):
        print('Vehicle change 7 gear')

# Car Object
obj_car=Car('Car x1','Red',2000000)
obj_car.show()
#calls methods from car class
obj_car.max_speed()
obj_car.change_gear()

# Vehicle Object
obj_vehicle=Vehicle('Truck x1','white',7500000)
obj_vehicle.show()
# calls methods from a Vehicle class 
obj_vehicle.max_speed()
obj_vehicle.change_gear()

