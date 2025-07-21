# wap that create class with class method and normal methods that print details like name, age, gender also use constructor to print details
class Student:
    full_name = "Ayush Himalaya Shrestha"
    age = 27
    gender= "male"
    
#normal method
    

#classmethod
    @classmethod
    def printDetails(cls):
        print(f"My Name is {cls.full_name} , age is {cls.age} and gender is {cls.gender}")

Student.printDetails()


