class student:
    student_name = ""
    student_age = 0
    student_marks = 0
    def __init__(self,age,name,marks):
        self.student_age = age
        self.student_name = name
        self.student_marks = marks
        print("constructor called")

    def display_student_details(self):
     print("student", self.student_name, self.student_age,self.student_marks)


student1 = student(45, "john", 80)
student1.display_student_details()

class person:
    age = ""
    name=""
    def __init__(self,name,age):
        self.name =name
        self.age =age

    def display_person_details(self):
     print("person", self.name,self.age)


class student(person):
    uniform=""
    def __init__(self,name,age,uniform):
        super().__init__(name,age)
        self.uniform = uniform
    def display_students_details(self):
        print("students",self.uniform)

student1 = student("jimmy","18","jeans")
student1.display_students_details()
student1.display_person_details()
"""
class animal:
    def __init__(self):
        pass
    def speak(self):
        pass
class dog(animal):
   def __init__(self):
       pass
   def speak(self):
     print("i am a dog and i bark",)

class cat(animal):
 def __init__(self):
   pass
 def speak(self):
     print("i am a cat and i meow",)

dog1=dog
dog1.speak()
cat1 = cat
cat1.speak()
"""

class Bankaccount:
    balance=0
    account_name=""
    def __init__(self):
        pass
    def withdraw(self,amount):
        self.balance-=self.balance-amount
        return self.balance
    def transfer(self,amount):
        self.balance=self.balance-amount
        return self.balance
    def deposit (self,amount):
        self.balance = self.balance+amount
        return self.balance
    def show_balance(self):
        print("The details are:Name-", self.account_name, "balance", self.balance)

account1=Bankaccount()
account1.balance=100
account1.account_name="jimmy"
account1.show_balance()


