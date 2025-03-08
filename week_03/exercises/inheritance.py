# # # # #python OOP inheritance

# # # # #The Kingdom Analogy

# # # # class Character:
# # # #     def __init__(self, name, health):
# # # #         self.name = name
# # # #         self.health = 100

# # # #     def attack(self):
# # # #         print(f"{self.name} attacks!")

# # # # class Knight(Character):
# # # #     def attack(self):
# # # #         print(f"{self.name} slashes with a sword!")

# # # # class Archer(Character):
# # # #     def attack(self):
# # # #         print(f"{self.name} shoots an arrow!")

# # # # class Healer(Character):
# # # #     def heal(self, other):
# # # #         other.health += 10
# # # #         print(f"{self.name} heals {other.name}!")

# # # # characters = [Knight("Arthur", 100), Archer("Robin", 80), Healer("Merlin", 70)]

# # # # for char in characters:
# # # #     char.attack()

# # # # """ 
# # # #            Character
# # # #           /    |     \
# # # #       Knight  Archer  Healer

# # # #  """    


# # # # suppost we build software for trasnportaion company

# # # class Vehicle:
# # #     def __init__(self, brand, model):
# # #         self.brand = brand
# # #         self.model = model

# # #     def move(self):
# # #         print(f"{self.brand} {self.model} is moving.")


# # # class Car(Vehicle):
# # #     def move(self):
# # #         print(f"{self.brand} {self.model} is driving.")

# # # class Truck(Vehicle):
# # #     def move(self):
# # #         print(f"{self.brand} {self.model} is hauling loads.")

# # # class Bike(Vehicle):
# # #     def move(self):
# # #         print(f"{self.brand} {self.model} is riding.")


# # # vehicles = [Car("Toyota", "Camry"), Truck("Ford", "F-150"), Bike("Giant", "Escape")]

# # # for vehicle in vehicles:    
# # #     vehicle.move()

# # #     print(f"Vehicle type: {type(vehicle).__name__}")



# # # mutiple inheritance

# # class Father:
# #     hair_color = "brown"
# #     eye_color = "green"
# #     height = 6.5


# # class Mother:
# #     hair_color = "blonde"
# #     eye_color = "blue"


# # class Child(Mother,Father):
    
# #     def __init__(self):
# #         print(self.hair_color)
# #         print(self.eye_color)
# #         print(self.height)


# # child = Child()


# # #multi level inheritance

# # class Grandfather:
# #     hair_color = "brown"
# #     eye_color = "green"
# #     height = 6.5


# # class Father(Grandfather):
# #     hair_color = "blonde"
# #     eye_color = "blue"


# # class Child(Father):
    
# #     def __init__(self):
# #         print(self.hair_color)
# #         print(self.eye_color)
# #         print(self.height)

# #dimond problem
# """ 
#       A
#      / \
#     B   C
#      \ /
#       D

#  """

# class Grandma:
#     grandma_name = "Alice"
#     def do_somthing(self):
#         print("Grandma does something")

# class Branda(Grandma):
#     def do_somthing(self):
#         print("Branda does something")

# class Branc(Grandma):
#     def do_somthing(self):
#         print("Branc does something")


# class BrandaBranc(Branc,Branda):
#     def __init__(self):
#        print(self.grandma_name)
#     pass

# branda_branc = BrandaBranc()

# branda_branc.do_somthing()


