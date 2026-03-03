class Car:
    total_car = 0

    def __init__(self,brand,model):
        self.__brand = brand
        self.__model = model
        Car.total_car += 1

    def get_brand(self):
        return self.__brand
    
    def display(self):
        return f"Brand: {self.__brand}, Model: {self.__model}"
    
    def fuel_type(self):
        return "Petrol or diesel"
    
    @staticmethod
    def general_description():
        return "Cars are a mean of transport"
    
    @property
    def model(self):
        return self.__model
    
    

class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Eletric charge"


c1 = Car("Toyota","Corolla")
# print(c1.brand,c1.model)
# print(c1.display())

# print(c1.get_brand())
# print(c1.fuel_type())
# print(Car.total_car)
# print(c1.general_description())
# print(Car.general_description())
# c1.model = "city"
# print(c1.model)

c2 = ElectricCar("Tesla","Model S","85KWH")
# print(c2.model)
# print(c2.display())
# print(c2.fuel_type())
# print(isinstance(c2,Car))
# print(isinstance(c2,ElectricCar))



class Battery:
    def battery_info(self):
        return "this is battery"

class Engine:
    def engine_info(self):
        return "this is engine"

class ElectricCarTwo(Battery,Engine,Car):
    pass


my_tesla = ElectricCarTwo("tesla","model s")
print(my_tesla.battery_info())
print(my_tesla.engine_info())