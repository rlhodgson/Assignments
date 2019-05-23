class Point: #creates a new type, point
    def __init__(self, x, y): #initialises the class role, self has to be first then parameters
        self.x = x #must define that self.parameter is the parameter
        self.y = y
        
    def __str__(self): #can have functions in and out of the class, this is a method of the class now
        return ("Points are: {}, {}".format(self.x, self.y))
        
p = Point(1, 2) #like calling a function but sets these into the class
print(p) #calls the "method" which is a function in the class


class Colour:
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue
        
    def __str__(self): #can have functions in and out of the class, this is a method of the class now
        return ("Colours({}, {}, {})".format(self.red, self.green, self.blue))     
        
    def __repr__(self):
        return ("r = {0}, g = {1}, b = {2}".format(self.red, self.green, self.blue))
    
    def lightness(self):
        """Returns the ligthness on a scale of 0 -1"""
        min_component = min(self.red, self.green, self.blue)
        max_component = max(self.red, self.green, self.blue)
        avg = (max_component + min_component) / 2
        light = avg / 255
        return light
    
    def __add__(self, other):
        """Returns the new colour of two added"""
        red = min(255, self.red + other.red)
        green = min(255, self.green + other.green)
        blue = min(255, self.blue + other.blue)
        return Colour(red, green, blue)
        
c = Colour(200, 123, 50)
print(repr(c))
print(c.lightness())
c1 = Colour(200, 20, 60)
c2 = Colour(9, 76, 40)
print(c1 + c2)