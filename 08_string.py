# In Python, anythhing that you enclose between single or double quotation marks is considered a string.

name = "Niket"
frind = "Harry"
anotherfrind = 'lovish'
print("Hello," + name)

apple = '''He said,
Hi Harry
hey I am good
"I want to eat an apple'''
print(apple)

print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
# print(name[5])   # Throws an error

print("Lets use a for loop\n")
for character in apple:
    print(character)