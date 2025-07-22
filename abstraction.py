from abc import ABC, abstractmethod

# tea -> milk , blacktea
class Tea(ABC):
    def takingOrder(self):
        return "Taking Order"
    @abstractmethod
    def makeTea(self):
        pass
    @abstractmethod
    def addMaterials(self):
        pass
    @abstractmethod
    def pour(self):
        pass
    @abstractmethod
    def serve(self):
        return "serve"
    
    def process(self):
        takingOrder = self.takingOrder()
        makeTea =self.makeTea()
        addMaterials=self.addMaterials()
        pour = self.pour()
        serve =self.serve()
        return f"{takingOrder}\n {makeTea}\n {addMaterials}\n {pour}\n {serve}"
class MilkTea(Tea):
    def makeTea(self):
        return "Make Milk Tea"
    def addMaterials(self):
        return "Add milk, sugar, teabag"
    def pour(self):
        return "Pour in cup"
    def serve(self):
        return "Served"

class BlackTea(Tea):
    def makeTea(self):
        return "Make Black Tea"
    def addMaterials(self):
        return "Add lemon, sugar, teabag"
    def pour(self):
        return "Pour in cup"
    def serve(self):
        return "Served"
    
one=MilkTea()
print(one.process())