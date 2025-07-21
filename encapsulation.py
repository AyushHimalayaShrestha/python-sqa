# encapsulation -> the way of hiding properties
# _ , __ -> hide

class Parent:
    def __init__(self,firstname,middlename, lastname):
        self.firstname=firstname
        self.middlename=middlename
        self.__lastname=lastname #private sector

    def getLastName(self):
        return self.__lastname
    
    @property
    def lastname(self):
        return self.__lastname
    
    @lastname.setter
    def lastname(self, lastname):
        self.__lastname =lastname

    def setLastName(self, lastname):
        self.__lastname =lastname

    def _full_details(self):  # protected
        return f"{self.firstname} {self.middlename} {self.__lastname}"

    def printinfo(self):
        return self._full_details() 

child1 =Parent("Ayush","Himalaya","Shrestha")
print(child1.firstname)
print(child1.middlename)
print(child1.getLastName())
child1.setLastName("Himalaya Shrestha")
print(child1.getLastName())

print(child1.printinfo())
# print(child1._full_details()) -> protected method

child1.lastname ="Palanchoke"
print(child1.lastname)