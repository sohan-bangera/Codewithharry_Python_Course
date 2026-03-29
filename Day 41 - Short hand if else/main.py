a = 330
b = 3303
print("A") if a > b else print("=") if a ==b else print("B")

'''
How the python groups the above condition
print("A") if a > b else print("=") if a == b else print("B")
print("A") if a > b else [print("=") if a == b else print("B")]
print("A") if a > b else [Unit 1]
'''

a = 330
b = 3303
print("A") if a > b else print("=") if a < b else print("B") if a==b else print("D")

'''
How does python groups the above condition
print("A") if a > b else print("=") if a < b else [print("B") if a==b else print("D")]
print("A") if a > b else [print("=") if a < b else [Unit 1]]
print("A") if a > b else [unit 2]
'''