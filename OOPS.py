class Dog:
    species = "Canis familiaris"
    def __init__(self,name,age):
        self.name=name
        self.age=age
        #self.breed = breed 
    def description(self):# Instance method
        return f"{self.name} is {self.age} old "
    def speak(self, sound="Bla Bla"):# Instance method
        return f"{self.name} barks {sound}"
    


class cat:
    def __init__(self):
        self.name="donny"
        self.age=15
    def description(self):
        return f"{self.name} is {self.age} old "        
    
#inheritance

class GreatDain(Dog):
    def speak(self, sound="Arf"):
        #return f"{self.name} says {sound}"
        return super().speak(sound="Din Don")
    

class Puddle(Dog):
    pass    

miles = Dog("Miles", 4 )
Dain = Dog("Tony",25)
pepe = Puddle("Tiny",13)
donny=cat()
#miles =GreatDain("miles", 5 )
#inheritance
Stephan=GreatDain("Stephan",10)

#You can only run this in a pyhton interpreter
#exec(open("OOPS.py").read())
#super(GreatDain, Stephan).speak("Bla bla bla")
