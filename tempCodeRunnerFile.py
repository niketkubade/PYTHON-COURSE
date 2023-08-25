# Strings are immutable
a = "niket"
print(len(a))
print(a.upper())
print(a.lower())

# rstrip() removes any trailing character. Example:
b = "harry!!!!!!!! !!!!! harry"
print(b.rstrip("!"))

# replace() :
print(b.replace("harry","John"))

# split():the method spits the given string at the specified instance and returns the separated strings as list items:
print(b.split(" "))

# Capitalize() :method turns only the first character of the string to uppers case and all other to lower case.
blogHeading = "introduction to js"
print(blogHeading.capitalize())

# Center(): method aligns the string to the center as per the parameters givern by the user.
str1 = "Welcome to the Console!!!"
print(len(str1))
print(len(str1.center(50)))

# Count():
print(b.count("harry"))

# endswith (): method checks if the string ends with given value. If yes then return True, else False.
str1 = "Welcome to the Console!!!"
print(str1.endswith("!!!"))
str1 = "Welcome to the Console!!!"
print(str1.endswith("to",4,10))

# Find():
str1 = "He's name is Dan. He is an honest man."
print(str1.find("is"))
 
 # isalnum(): method  returns True only string only consist of A-Z,a-z,0-9.if any other consist then returns false.
str1 = "WelcomeToTheConsole"
print(str1.isalnum()) 
# isalpha() :
str1 = "Welcome"
print(str1.isalpha())
# islower() :
str1 = "hello world"
print(str1.islower())
# isprintable() :
str1 = "we wish you a Mery christmas\n"
print(str1)
print(str1.isprintable())
# isspace(): method return True only and only if the string contains white spaces.else returns false.
str1 = "        "  #using spacebar
print(str1.isspace())
str2 = "        "  #using tab
print(str2.isspace())
# istittle() : returns True only if the first letter of each word of the string is capitalized,else return false.
str1 = "World Health Organization"
print(str1.istitle())
str2 = "To kill a Mocking bird"
print(str2.istitle())
# isupper(): same like islower
# startswith(): 
str1 = "Python is a Interpreted Language"
print(str1.startswith("Python"))