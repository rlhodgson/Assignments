"""Test to work backwards"""
class Thing:
    """Gives info on a thing"""
    def __init__(self, name, height, words):
        """Initialises class code"""
        self.name = name
        self.height = height
        self.words = words
        
    def taller_by(self, amount):
        """Increases height"""
        self.height += amount
        
    def learn(self, list_words):
        """Adds words to the list of known words"""
        for word in list_words:
            self.words.append(word)
            
    def __str__(self):
        """The print string"""
        if len(self.words) > 0:
            strings = [str(word) for word in self.words]
            res = str(", ".join(strings))
            second = ("Hi. I'm {}. I'm {} cm tall.\nWords I know: {}.".format(self.name, 
                                                                              self.height, res))
        elif len(self.words) <= 0:
            second = ("Hi. I'm {}. I'm {} cm tall.\nWords I know:".format(self.name, self.height))
        return second
    
another = Thing("Donald", 40, ["quack", "quack"])
print(another)
another.taller_by(1)
another.learn(['quack'])
print(another)


