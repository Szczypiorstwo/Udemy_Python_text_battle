import re

string = "'I AM NOT YELLING' she said. Though we knew it not to be truth."

#re.sub( things we want to modify, things that we want to replace with (empty if we want to remove things from first
# parameter), sring that we want to manipulate )
new = re.sub('[A-Z]', '', string) # for removing capital letters from A to Z
new2 = re.sub('[a-z]', '', string) # for removing small letters from a to z
new3 = re.sub('[\',.-]', '', string) # form removing special characters defined

new4 = re.sub('[\',-.A-Za-z]', '', string) # form removing special characters defined,small and capital letters, spaces left
new5 = re.sub('[" "]', '', string) # removing spaces

print(new)
print(new2)
print(new3)
print(new4)
print(new5)

string2 = string + "9-0085-365"

print(string2)

new6 = re.sub('[0-9]', '', string2) # removing all numbers
new7 = re.sub('[^0-9]', '', string2) # removing all except numbers

print(new6)
print(new7)