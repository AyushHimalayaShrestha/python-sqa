# parent -> properties and methods -> child

class Parent:
    #lastname = "Himalaya Shrestha"
    def __init__(self,lastname):
        self.lastname =lastname
        print("Hello from parent")
    def printLastName(self):
        print(self.lastname)
        
class Child(Parent):
   # firstname ="Ayush"
   def __init__(self, firstname,lastname):
      super().__init__(lastname)
      self.firstname=firstname
      print("Hello from Child")
   def PrintDetails(self):
        print(f"Hello {self.firstname} {self.lastname}")

obj1=Child("Ayush","Himalaya Shrestha")
obj1.PrintDetails()
obj1.printLastName()

obj2=Child("Surendra","Himalaya")
obj2.PrintDetails()
obj2.printLastName()