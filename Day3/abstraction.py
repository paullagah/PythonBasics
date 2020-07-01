from abc import ABC, abstractmethod

class Animal:
    @abstractmethod
    def eat(self):
        pass

class Mammal(Animal):
    def eat(self):
        print("nom nom")