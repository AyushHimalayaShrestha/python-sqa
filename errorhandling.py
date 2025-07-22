# try except else finally
try:
    print(10/0)
#except ZeroDivisionError:
 #   print("cannot divide by zero")

except Exception as e:
    print(e)
else:
    print("no error found")
finally:
    print("This is finally block")