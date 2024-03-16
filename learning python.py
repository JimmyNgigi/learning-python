#python comments-(this is a single line comment)
"""
this is a multi-line comment
"""
#variables
student_name = "<jimmy>"#string data type
student_age =20 #data type integer
student_score =100
student_fee =200
print(student_name,)
print(student_age)
print(student_score)
print(student_fee)

book_price =300 #valid variable name
_book_price = 400 #valid variable name
print(book_price)

x=y=z = 20 #one value multiple variables
print(x,y,z)
x,y,z =10,20,30 #multiple values with multiple variables
print(x,y,z)
firstname ="jimmy"
lastname ="ngigi"
thirdname ="jimmy" "ngigi"
print("my third name is:",thirdname)
"""
this is casting
"""
price=10
qty=3
total=price*qty
myanswer1="the total is "+str(total)+"kenya shillings"
print(myanswer1)

firstname="jimmy"
secondname="77"
thirdname=firstname+" "+str(secondname)+""
print(thirdname)

print(5//2)

age=50
nationality="kenyan"
if nationality=="kenyan"and age>=35:
    print("can be president")
else:
    print("not president")

constituency="kasarani"
if constituency=="kasarani" or constituency=="westlands" or constituency=="parklands":
    print("you can governor")
else:
    print("can not governor")

y=270
if y%2==0:
    print("is an even number")
else:
    print("is an odd number")

"""
loops and continue

x = 0
while x < 5:
 x += 1
 if x == 3:
   continue
 print(x)
 """
"""
x = 0
while x < 5:
  if x ==3:
         break
print(x)
"""
"""
country=input("Enter the country:")
if country=="kenya":
    print("east african")
elif country=="ethiopia":
     print("east african")
elif country=="tanzania":
     print("east african")
elif country=="uganda":
     print("east african")
else:
     print("unknown country")
"""

"""
x=1
while x<=10:
    print(x)
    x+=1
    if(x==3):
        break
else:
    print("loop  ended")
print("ended")
"""
"""
number = 1
sum_of_odds = 0
while number <=10:
    if number %2 == 1:
        sum_of_odds += number
        number+=1
        print("sum of odds is",sum_of_odds)
"""
"""
for x in range(1,6,2):
  print(x)
"""
"""
fruits = ["apple","banana","passion"]
for fruit in fruits:
    print(fruit)
"""
"""
total=0
for number in range(1,10,2):
    total+=number
print("sum_of_odds is",total)
"""
input=[input("Enter your name:"),input("Enter your name:"),input("Enter your name:")]
print(input)


