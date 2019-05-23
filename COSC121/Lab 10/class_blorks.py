class Blork:
    """Defines the Blork class.
    Data attributes: name of type str
                     height (metres) of type float
                     has_horns of type bool    
    """

    def __init__(self, name, height, has_horns=False, baranges=0):
        """Blork constructor"""
        self.name = name
        self.height = height
        self.has_horns = has_horns
        self.baranges = baranges
        
    def say_hello(self):
        """Prints hello based on the confidence of the blork"""
        if self.has_horns == True:
            print("HI! MY NAME IS {}!".format(self.name.upper()))
        elif self.has_horns == False:
            print("Hi! My name is {}!".format(self.name))
            
    def __str__(self):
        """Prints accordnig to if the blork has horns"""
        if self.has_horns == True:
            return ("{} is a {:.2f} m tall horned blork!".format(self.name, self.height))
        elif self.has_horns == False:
            return ("{} is a {:.2f} m tall blork!".format(self.name, self.height))
        
    def collect_baranges(self, number=1):
        """Counts the number of baranges"""
        self.baranges += number
        return self.baranges
    
    def eat(self):
        """Eats a barange"""
        if self.baranges < 1:
            print("I don't have any baranges to eat!")
        elif self.baranges >= 1:
            self.baranges -= 1
            self.height += 0.1
    
    def feast(self):
        """Removes stuff from when they eat a lot"""
        if self.baranges < 5:
            print("I don't have enough baranges to feast!")
        elif self.baranges >= 5 and self.has_horns == False:
            self.baranges -= 5
        elif self.baranges >= 5 and self.has_horns == True:
            self.baranges -= 5
            increase = self.height / 2
            self.height += increase     
            
mighty_blork = Blork("Chewblorka", 3.14, True)
print("Baranges: {}".format(mighty_blork.baranges))
mighty_blork.collect_baranges(9)
print("Baranges: {}".format(mighty_blork.baranges))
mighty_blork.feast()
print("Baranges: {}".format(mighty_blork.baranges))
print(mighty_blork)