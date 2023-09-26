class Person(): #Class to distribute the diffrent methods
    def __init__(self, name, age, gender): #The constructor (special method) to declare all changing (and non changing variables)
        self.name = name #name variable
        self.age = int(age) #age variable
        self.gender = gender #gender variable

    def Cname(self, name): #name method for changing names
        self.name = f"{name}"

    def Cage(self, age): #age method for changing age
        self.age = f"{age}"

    def Cgender(self, gender): #gender method for changing gender
        self.gender = f"{gender}"

    def __str__(self): #special method to get a print output in a tolerable format
        return f" Name: {self.name}, Age: {self.age}, Gender: {self.gender}"

Per = Person('John', 55, 'Male') #Calling on the class
print(Per) #Printing the inital statements
print(' -- ')
Per1 = Per.Cname('Jeanette')
Per2 = Per.Cage(23)
Per3 = Per.Cgender('Female')
print(Per)
"""
Output: python3 class_people.py
 Name: John, Age: 55, Gender: Male
 --
 Name: Jeanette, Age: 23, Gender: Female
"""
