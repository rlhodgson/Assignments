"""File for creating Person objects"""

class Person:
    """Defines a Person class, suitable for use in a hospital context.
    Data attributes: name of type str
                     age of type int
                     weight (kg) of type float
                     height (metres) of type float
    Methods: bmi()
    """

    def __init__(self, name, age, weight, height):
        """Creates a new Person object with the specified name, age, weight
           and height"""
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height

    def bmi(self):
        """Returns the body mass index of the person"""
        bmi = float(self.weight) / (float(self.height) * float(self.height))
        return bmi
    
    def status(self):
        """Returns the status fo someone's health based on their bmi"""
        bmi_num = self.bmi()
        if bmi_num < 18.5:
            status = "Underweight"
        elif bmi_num >= 18.5 and bmi_num < 25:
            status = "Normal"
        elif bmi_num >= 25 and bmi_num < 30:
            status = "Overweight"
        elif bmi_num >= 30:
            status = "Obese"
        return status
    
    def __str__(self):
        """Returns the formatted string represent of the Person object"""
        name = self.name
        age = self.age
        bmi = self.bmi()
        status = self.status()
        template = "{0} ({1}) has a bmi of {2:3.2f}. Their status is {3}."
        return template.format(name, age, bmi, status)    
    
def read_people(csv_filename):
    """Returns lists of peoples info"""
    infile = open(csv_filename)
    lines = infile.readlines()
    full_lines = []
    for line in lines:
        name, age, weight, height = line.split(',')
        words = Person(name, age, weight, height)
        full_lines.append(str(words))
    return full_lines

def filter_people(people, status_string):
    """Filters the list of people"""
    status_people = []
    for human in people:
        if status_string in human:
            status_people.append(human)
    return status_people

  
bods = read_people("people1.csv")
for status_string in ['Underweight', 'Normal', 'Overweight', 'Obese']:
    bods_with_status = filter_people(bods, status_string)
    print("People who are {}:".format(status_string))
    for bod in bods_with_status:
        print(bod)
    print()