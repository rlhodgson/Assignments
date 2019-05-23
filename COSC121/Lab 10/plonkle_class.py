"""This is a plonkle class"""
class Plonkle:
    """Defines some values including their health and name etc"""
    def __init__(self, grade, name, health):
        """Initialises the class code"""
        self.grade = grade
        self.name = name
        self.health = health
        
        grades = ['Grubling', 'Throve', 'Plaguelet']
        if self.grade not in grades:
            raise ValueError('Invalid Plonkle grade')
        
        if self.health < 0:
            self.health = 0
            
    def __str__(self):
        """String method for the plonkles"""
        return ("{} ({}), health = {:.1f}".format(self.name, self.grade, self.health))
    
    def pain(self, amount):
        """The amount to be removed from the health"""
        self.health = max(0, self.health - amount)
        return self.health
            