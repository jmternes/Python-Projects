from abc import ABC, abstractmethod

class Animal(ABC):
    def talk(self):
        print("I am a human, I can talk.")

    @abstractmethod
    def typeOfSkin(self):
        print("We can identify the types of skin for different animals.")
        pass

class Dog(Animal):
    def typeOfSkin(self):
        print("I usually have fur.")

class Snake(Animal):
    def typeOfSkin(self):
        print("I have scales.")

class Shark(Animal):
    def typeOfSkin(self):
        print("I have smooth skin.")

puppy = Dog()
puppy.typeOfSkin()
    
