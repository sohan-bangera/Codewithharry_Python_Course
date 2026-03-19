a = "Sohan"
b = a.upper()

print(b, a)
print(a.lower())
c = "SohanMMMMM MMMMMMM"
print(c.rstrip("M"))
d = " Hall "
print(d.strip())

blog = "introduction tO the progrAmming langauge python"
print(blog.capitalize())
print(c.split(" "))
print(blog.center(100, "-"))

print(len(blog))
print(len(blog.center(100)))
a1 = "--------------------------introduction tO the progrAmming langauge python---------------------------"
print(len(a1))
print(a1.count("i"))

str1 = "Welcome to the Console !!!"
print(str1.endswith("!!!"))

str1 = "Welcome to the Console !!!"
print(str1.endswith("to", 4, 10))

str1 = "WelcomeToThe12Console"
print(str1.isalnum())

str1 = "Welcome"
print(str1.isalpha())

# \n \t \r are not printable
str1 = "We wish you a Merry Christm\nas"
print(str1.isprintable())

str1 = "        "       #using Spacebar
print(str1.isspace())
str2 = "   2     "       #using Tab
print(str2.isspace())

str1 = "World Health Organization" 
print(str1.istitle())

str1 = "Python is a Interpreted Language" 
print(str1.swapcase())

str1 = "He's name is Dan. Dan is an honest man."
print(str1.title())