# Student Class with Methods
class Students:
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade
    def display_info(self):
        print(f'Name :{self.name}, Age : {self.age}, Grade:{self.grade}')
s1 = Students('Ayush',28,'A')
s1.display_info()

s2 =Students('Ram',20,'B')
s2.display_info()
