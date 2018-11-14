
#function with infinite number of parameters, people is stored as an array
def print_person(*people):
    for person in people:
        print("This is person",person)

print_person("Michał","Adam","Jo","Nishikori")

#function with default agruments
def print_name_and_age(name = "Someone",age = "Unknown"):
    print("This is name",name,"and this is age:",age)

print_name_and_age("Nick",27)
print_name_and_age("nick")
print_name_and_age(age=25)
print_name_and_age()


#function with return value
def do_math(num1, num2):
    return num1+num2

do_math(5,7)

math1 = do_math(2,7)
math2 = do_math(5,10)

print("First result is:",math1,"and second result is:",math2)