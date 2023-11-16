class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  
  def __str__(self):
    return f"Name: {self.name}, Age = {self.age}"
  def myfunc(self):
    print("Hello my name is " + self.name)
    

p1 = Person("John", 36)
p2 = Person("J.Sheon",32)
#p3= Person(input("請輸入名字:  "),input("請輸入年齡:  "))

print(p1)
print("Name:",p2.name,",","Age =",p2.age)
print("\n")
#print(p3)
p1.myfunc()
