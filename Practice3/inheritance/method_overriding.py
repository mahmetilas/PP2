class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def speak(self):     # переопределение
        print("Dog barks")

d = Dog()
d.speak()
# --------------------------------------------------------------------------------------------------------------------------
class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    def speak(self):
        super().speak()     # вызов родителя
        print("Dog barks")

Dog().speak()