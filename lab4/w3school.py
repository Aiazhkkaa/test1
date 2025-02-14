# #Python Iterators

# class MyNumbers:
#   def __iter__(self):
#     self.a = 1
#     return self

#   def __next__(self):
#     if self.a <= 20:
#       x = self.a
#       self.a += 1
#       return x
#     else:
#       raise StopIteration

# myclass = MyNumbers()
# myiter = iter(myclass)

# for x in myiter:
#   print(x)

# #Python Polymorphism

# class Car:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model

#   def move(self):
#     print("Drive!")

# class Boat:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model

#   def move(self):
#     print("Sail!")

# class Plane:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model

#   def move(self):
#     print("Fly!")

# car1 = Car("Ford", "Mustang")       #Create a Car object
# boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
# plane1 = Plane("Boeing", "747")     #Create a Plane object

# for x in (car1, boat1, plane1):
#   x.move()

# #Python Scope

# x = 300

# def myfunc():
#   print(x)

# myfunc()

# print(x)

# #Python Modules

# import mymodule as mx

# a = mx.person1["age"]
# print(a)

# #Python Datetime

# import datetime

# x = datetime.datetime.now()

# print(x.year)
# print(x.strftime("%A"))

# #Python Math

# import math

# x = math.sqrt(64)

# print(x)

# #Python JSON

# import json

# x = {
#   "name": "John",
#   "age": 30,
#   "city": "New York"
# }

# y = json.dumps(x)

# print(y)