#parent
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")

#child
class Dog(Animal):
    def speak(self):
        print(f"{self.name} barks")

    def fetch(self):
        print(f"{self.name} fetches a ball")

#child2
class Cat(Animal):
    def speak(self):
        print(f"{self.name} meows")

    def scratch(self):
        print(f"{self.name} scratches")

#overload
class Labrador(Dog):
    def speak(self, sound="bark"):
        print(f"{self.name} {sound}")

animal = Animal("Generic Animal")
dog = Dog("Buddy")
cat = Cat("Whiskers")
labrador = Labrador("Rusty")

#override
animal.speak()
dog.speak()
cat.speak()

labrador.speak()
labrador.speak("woof")

dog.fetch()
cat.scratch()
