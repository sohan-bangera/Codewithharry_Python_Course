def my_geneyyyrator():
    for i in range(5):
        yield i

gen = my_geneyyyrator()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))