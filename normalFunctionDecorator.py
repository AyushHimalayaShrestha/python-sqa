def addMethods(fixed_vlaue):
    def decorators(func):
        def wrapper(*agrs,**kwargs):
            results =func(*agrs,**kwargs)
            return results +fixed_vlaue
        return wrapper
    return decorators
@addMethods(10)
def AddNumber(a):
    return a

@addMethods(20)
def AddNumbers(b):
    return b



print(AddNumber(20))
print(AddNumbers(30))