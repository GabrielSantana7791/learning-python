from classes.animal import Animal

class Dog(Animal):
    def __init__(self, name, color, race):
        super().__init__(name, color)
        self.race = race

    def bark(self):
        print("auau")        