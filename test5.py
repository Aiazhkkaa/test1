#python booleans

a = 350
b = 50
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#python operators

print(9 + 6 - 2 + 7)

#python lists
 
thislist = ["melon", "cherry", "grapes", "orange", "cherry"]
print(thislist)

#Access List Items

thislist = ["orange", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

#Change List Items

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:4] = ["blackcurrant", "watermelon"]
print(thislist)

#Add List Items

thislist = ["orange", "banana", "melon"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#Remove List Items

thislist = ["orange", "melon", "cherry"]
thislist.pop(1)
print(thislist)

#Loop Lists

thislist = ["orange", "banana", "kiwi"]
for x in thislist:
  print(x)

#List Comprehension

fruits = ["apple", "banana", "melon", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

#Sort Lists

thislist = [120, 32, 78, 83, 12]
thislist.sort()
print(thislist)

#Copy Lists

thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)

#Join Lists

list1 = ["b", "c" , "d"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)

#Python Tuples

tuple1 = ("orange", "banana", "cherry")
tuple2 = (6, 2, 5, 3, 9)
tuple3 = (True, False, False)

#Update Tuples

x = ("melon", "orange", "apple")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

#Unpack Tuples

fruits = ("kiwi", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

#Loop Tuples

thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])

 #Join Tuples

 tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

#Python Sets

set1 = {"apple", "orange", "kiwi", "apple"}

print(set1)

#Add Set Items

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

#Remove Set Items

thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)

#Loop Sets

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

#Join Sets

set1 = {"a", "b", "c"}
set2 = {5, 4, 3}

set3 = set1 | set2
print(set3)

#Python Dictionaries

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])

#Change Dictionary Items

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})

#Add Dictionary Items

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})

#Remove Dictionary Items

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)

#Loop Dictionaries

for x in thisdict.values():
  print(x)

#Copy Dictionaries  

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)

#Nested Dictionaries

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "ayazhan",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

#Python If ... Else

a = 288
b = 982
if b > a:
  print("b is greater than a")

# Python While Loops

i = 1
while i < 10:
  print(i)
  if i == 3:
    break
  i += 1

#Python For Loops

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)





