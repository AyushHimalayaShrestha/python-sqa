# Using *args and **kwargs
def show_details(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)

show_details(1, 2, 3, name="Ayush", language="Python")
