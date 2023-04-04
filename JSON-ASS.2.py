class Dog:
    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color        
    def description(self):
        print(f"{self.name} is {self.age} years old.") 
    def get_info(self):
        print(f"{self.name}'s coat color is {self.coat_color}.")
        
class JackRussellTerrier(Dog):
    def play_fetch(self):
        print(f"{self.name} loves to play fetch!") 
    def hunt(self):
        print(f"{self.name} is a skilled hunter.")
        
class Bulldog(Dog):
    def snore(self):
        print(f"{self.name} snores loudly.")
    def guard(self):
        print(f"{self.name} is a loyal and protective guard dog.")

dog1 = Dog("Rufus", 3, "brown")
dog2 = JackRussellTerrier("Max", 2, "white and brown")
dog3 = Bulldog("Spike", 4, "black")

dog1.description()
dog1.get_info()

dog2.description()
dog2.play_fetch()
dog2.hunt()

dog3.description()
dog3.snore()
dog3.guard()

