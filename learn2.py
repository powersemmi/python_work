class Car:

    def __init__(self, make, model, yaer):
        self.make = make
        self.model = model
        self.yaer = yaer
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.yaer) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometr(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can`t roll back an odometer!")


class ElectricCsr(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)


my_tesla = ElectricCsr('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
print(0.4 - 0.1)
