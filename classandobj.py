# Class and Object
# class -> template to create object
class One:
     #2 properties -> name and age
    name = "Ayush"
    age = 27
   
    # methods -> function in class -> self
    def PrintDetails(self,name,age):
       print(f"hello {self.name} your age is {self.age}")

    def PrintDetails(self,name, age):
        print(f"Hello {name} your age is {age}")
        
    # Constructor ->sepcial methods
    def __init__(self):
        print("this is constructor")

# object -> instance of the class
one = One()
print(one.name)
one.PrintDetails("hari",20)
print(one.age)
one.PrintDetails("Ram",30)
print(One.name)

