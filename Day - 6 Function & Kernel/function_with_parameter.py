print("Function with no parameter : ")
def greet():
    print("Harsh")
    print("Vipesh")
    print("Turakhia\n")
greet()
 
 
print("Function with single parameter : ")
def greet_with_name(name):
    print(f"Hello {name}\n")
greet_with_name("Harsh")


print("Function with multiple parameter : ")
def greet_with_name_and_loc(name, loc):
    print(f"Hello {name}")
    print(f"You are from {loc}\n")
greet_with_name_and_loc("Harsh", "Junagadh")


print("Keywords Arguments : ")
greet_with_name_and_loc(loc = "Junagadh", name = "Harsh")