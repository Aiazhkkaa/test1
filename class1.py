# #1

# class test1:
#     def getstring(self):
#         self.text = input()
#     def printstring(self):   
#         print(self.text.upper())

# text = test1()
# text.getstring()
# text.printstring()

# #2

# class Shape:
#     def area(self):
#         return 0

# class Square(Shape):
#     def __init__(self,lenght):
#         self.lenght = lenght

#     def area(self):
#         return self.lenght**2

# p1 = Shape()
# p2 = Square(10)

# print("Shape area:", p1.area()) 
# print("Square area:", p2.area())

# #3
# class Rectangle(Shape):
#     def __init__(self,lenght,width):
#         self.lenght = lenght
#         self.width = width

#     def area(self):
#         return self.lenght * self.width

# p3 = Rectangle(5,10)
# print("Rectangle area:", p3.area())

# #4
# class Point:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y

#     def show(self):
#         print(f"Point: x = {self.x} , y = {self.y}")

#     def move(self, new_x, new_y):
#         self.x = new_x
#         self.y = new_y

#     def dist(self, other_point):
#         return ((self.x - other_point.x)**2 + (self.y - other_point.y)**2 )**0.5

# p1 = Point(3, 4)
# p2 = Point(6, 8)

# p1.show()  
# p2.show()  

# print("Distance:",p1.dist(p2))  

# p1.move(10, 12)
# p1.show() 

# #5

# class Account:
#     def __init__(self, owner, balance=0):
#         self.owner = owner
#         self.balance = balance
#     def deposit(self, amount):
#             self.balance += amount
#             print(f"Deposited: {amount}. New balance: {self.balance}") 
#     def withdraw(self, amount):
#         if amount < self.balance:
#             self.balance -= amount
#             print(f"Withdrawn: {amount}. New balance: {self.balance}")
#         else:
#             print("You don't have that kind of money ")
#     def __str__(self):
#         return f"Account owner: {self.owner}\nAccount balance: {self.balance}"        

# acc = Account("Alice", 100)
# print(acc)

# acc.deposit(50)
# acc.withdraw(30)
# acc.withdraw(150) 

# #6
# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# numbers = [10, 15, 17, 19, 21, 23, 29, 30, 31, 37, 40]
# prime_numbers = list(filter(lambda x: is_prime(x), numbers))

# print("Prime numbers:", prime_numbers)













