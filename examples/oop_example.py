# oop_example.py
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a noise."

class Dog(Animal):
    def speak(self):
        return f"{self.name} barks."

def main():
    animal = Animal("Generic Animal")
    dog = Dog("Buddy")
    print(animal.speak())
    print(dog.speak())

if __name__ == "__main__":
    main()
