class Dog:
    species = "Canis familiaris"
    def __init__(self,name,age):
        self.name=name
        self.age=age
        #self.breed = breed 
    def description(self):# Instance method
        return f"{self.name} is {self.age} old "
    def speak(self, sound):# Instance method
        return f"{self.name} barks {sound}"
    
#inheritance

class GreatDain(Dog):
    def speak(self, sound="Arf"):
        #return f"{self.name} says {sound}"
        return super().speak(sound)
    

class Puddle(Dog):
    pass    

miles = Dog("Miles", 4 )
Dain = Dog("Tony",25)
pepe = Puddle("Tiny",13)
#miles =GreatDain("miles", 5 )
#inheritance
Stephan=GreatDain("Stephan",10)

#You can only run this in a pyhton interpreter
#exec(open("OOPS.py").read())
