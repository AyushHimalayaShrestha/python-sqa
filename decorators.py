class Student:
    name ="Hari"
    age =20
    gender ="male"

    @classmethod
    def PrintDetails(cls):
        print(f"My name is {cls.name} and age is {cls.age} and gender is {cls.gender}")

    @staticmethod
    def addNumbers(a,b):
        print(a+b)

    

Student.PrintDetails()
Student.addNumbers(30,40)


