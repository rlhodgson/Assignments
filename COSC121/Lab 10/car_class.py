"""Does stuff with a car"""
class Car:
    """Does more car stuff"""
    def __init__(self, model, year, speed=0):
        """Initialises the code"""
        self.model = model
        self.year = year
        self.speed = speed
        
    def accelerate(self):
        """Adds 5 to the speed"""
        self.speed += 5
        return self.speed
        
    def brake(self):
        """Takes off 5 unless speed is already 0"""
        if self.speed >= 5:
            self.speed -= 5
        elif self.speed == 0:
            self.speed = 0
        return self.speed
        
    def honk_horn(self):
        """Prints a string"""
        print("{} goes 'beep beep'".format(self.model))
        
    def __str__(self):
        """Returns a string"""
        return ("{} ({}), moving at {} km/h.".format(self.model, self.year, self.speed))
    
my_car = Car("Toyota", 1999, 50)
print(my_car)