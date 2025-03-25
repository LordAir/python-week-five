class Animal:
    def __init__(self, name):
        self.name = name
    
    def move(self):
        raise NotImplementedError("Subclasses must implement move()")

class Vehicle:
    def __init__(self, model):
        self.model = model
    
    def move(self):
        raise NotImplementedError("Subclasses must implement move()")

# Animal Subclasses
class Dog(Animal):
    def move(self):
        print(f"{self.name} the dog is 🐕 running on four legs!")

class Fish(Animal):
    def move(self):
        print(f"{self.name} the fish is 🐟 swimming through water!")

class Bird(Animal):
    def move(self):
        print(f"{self.name} the bird is 🦜 flying through the air!")

# Vehicle Subclasses
class Car(Vehicle):
    def move(self):
        print(f"{self.model} is 🚗 driving on the road!")

class Boat(Vehicle):
    def move(self):
        print(f"{self.model} is 🚤 sailing on water!")

class Airplane(Vehicle):
    def move(self):
        print(f"{self.model} is ✈️ flying through the sky!")

def showcase_movement(entities):
    print("\n=== Movement Showcase ===")
    for entity in entities:
        entity.move()
    print("=======================\n")

# Create instances
animals = [
    Dog("Buddy"),
    Fish("Nemo"),
    Bird("Polly")
]

vehicles = [
    Car("Toyota Corolla"),
    Boat("Speedster 2000"),
    Airplane("Boeing 747")
]

# Demonstrate polymorphic behavior
showcase_movement(animals)
showcase_movement(vehicles)

# Mixed demonstration
mixed_entities = [
    Dog("Rex"),
    Airplane("Airbus A380"),
    Fish("Dory"),
    Car("Tesla Model S")
]
showcase_movement(mixed_entities)
