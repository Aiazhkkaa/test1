#Python Functions
def my_function():
  print("Hello World")

my_function()

#Python Lambda
x = lambda a : a + 10
print(x(5))

#Python Arrays
cars = ["Ford", "Volvo", "BMW"]

#Python Classes/Objects
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()

#Python Inheritance
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

