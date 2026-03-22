#Before f string
letter = "Hi my name is {} and I am from {}"
name = "Sohan"
country = "India"

print(letter.format(name, country))

txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))

#Using F string
print(f"Hi my name is {name} and I am from {country}")

print(f"Hi my name is {{name}} and I am from {{country}}")


