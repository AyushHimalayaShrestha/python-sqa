class Hello:
    def __init__(self,name,age):
        print("Hello World From Constructor")
        self.full_name =name
        self.real_age =age
    

    def printDetails(self):
        return f"Hello World from method {self.full_name}"
hellos=Hello("ram",33)
print(hellos.printDetails())
hello1 = Hello("sita",23)
print(hello1.printDetails())