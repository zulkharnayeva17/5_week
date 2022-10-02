#Task 1
#example 1
class First:
    color = "red"

    def out(self):
        print(self.color +  "!")

class Second:
    color= "red"
    form="circle"

    def changecolor(self, newcolor):
        self.color =newcolor
    def changeform(self, newform):
        self.form =newform
obj1 = Second()
obj2 = Second()
print (obj1.color, obj1.form)
print(obj2.color, obj2.form)

obj1.changecolor("green")
obj2.changecolor("blue")
obj2.changeform("oval")
print (obj1.color, obj1.form)
print(obj2.color, obj2.form)

#changed 2 example
class Rectangle:
 def __init__(self, color = "green",  width =100, height = 100):
  self.color = color
  self.width = width
  self.height = height

 def square(self):
  return self.width * self.height

 def perimetr(self):
  return (self.width + self.height) * 2

rect1 = Rectangle()
print(rect1.color)
print(rect1.square())
print(rect1.perimetr())

rect1 = Rectangle("yellow", 23, 34)
print (rect1.color)
print(rect1.square())
print(rect1.perimetr())


#task 2
class Name:
 def __init__(self, first_name =input("Please enter  your name\n"),  last_name = input("please enter your last name\n")):
  self.first_name = first_name[0].upper() + first_name[1:len(first_name)].lower()
  self.last_name = last_name[0].upper() + last_name[1:len(last_name)].lower()



 def full_name(self):
  return self.first_name + " " + self.last_name



name1= Name()
print( "First name:", name1.first_name)
print("Last name:" , name1.last_name)
print("Full name: ",  name1.full_name())

#task 3
class Calculator:

 def addition(self):
  print(a + b)
 def difference(self):
  print(a - b)
 def multiplication(self):
  print(a * b)
 def division(self):
  print(a / b)


a = int(input("PLease, enter first number:\n"))
b = int(input("Please, enter first number:\n"))

obj = Calculator()
while True:
 print("1. addition")
 print("2. difference")
 print("3. multiplication")
 print("4. division")
 choice = int(input("Enter your choice:"))
 if choice == 1:
  print(obj.addition())
 elif choice == 2:
  print(obj.difference())
 elif choice == 3:
  print(obj.multiplication())
 elif choice == 4:
  print(obj.division())
 else:
  print("Invalid choice")
