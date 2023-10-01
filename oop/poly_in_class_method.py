class Ferrari:
    def fuel_type(self):
        print('petrol')

    def max_speed(self):
        print('max speed 350')

class BMW:
     def fuel_type(self):
        print('Diesel')

     def max_speed(self):
        print('max speed 240')

obj_ferrari=Ferrari()
obj_bmw=BMW()

# iterate objects of same type 
for car in (obj_ferrari,obj_bmw):
    car.fuel_type()
    car.max_speed()

