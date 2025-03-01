class Car:
    def __init__(self, make, model, year, color, milage, top_speed):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.milage = milage
        self.top_speed = top_speed
        #private attribute
        self.__no_of_wheels = 4


    def __str__(self):
        return f"{self.year} {self.make} {self.model}"
    #return "Hello World"

    def drive(self, km):
        print("Driving the car for", km, "km")

    def stop(self):
        print("Stopping the car")

    def move(self):
        self.drive()
        self.stop()

    #private method
    def __private_method(self):
        print("This is a private method")

    def get_no_of_wheels(self):
        self.__private_method()
        return self.__no_of_wheels
    
    def set_no_of_wheels(self, no_of_wheels):
        self.__no_of_wheels = no_of_wheels

