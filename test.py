"""
numbers = [1,3,7,19,25,20]
def my_function(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest
print("The largest number is ",my_function(numbers))
"""
fruits = ["apple", "banana", "orange", "grape","apple","pineapple","orange","grape","passion"]
fruits2 = set()
fruits3=[]
for fruit in fruits:
         if fruits.count(fruit)>1:
          fruits2 .add(fruit)
         else:
            fruits3.append(fruit)
print("the repeated fruits are",fruits2)
print("the fruits not repeated are",fruits3)

"""
stationery = ("books","pens","erasers","pencils")
print(stationery)
stationery =(list(stationery))
print(stationery)
stationery.append("rulers")
print(stationery)
stationery =(tuple(stationery))
print(stationery)

dictionery = {
"apple": "fruit",
"model": "mustang",
"year": 2000
 }
print(dictionery)

dictionery = {
"apple": "fruit",
"model": "mustang",
"year": 2000
 }
x = dictionery.values()
dictionery=["mustang"]
x=dictionery
print(x)

fruits = ["apple", "banana", "orange", "grape","apple","pineapple"]
numbers = [1,3,7,19,25,20]

set = {"apple", "banana",}
set.add("orange")
print(set)

set = {"apple", "banana","orange","grape",}
set.remove("orange")
print(set)
"""
