list = [ ['Q', 'A'], ['Q1', 'A1']]

list2 = list[0]
print(list2[1])
for i in list:
    print(i[1])

questions = [["What is the capital of india?", "Delhi"], ["Which is the number created by aryabatta?", "Zero"]]
amount = 0
for i in questions:
    print(i[0])
    userAnswer = input("Your Answer:")
    if userAnswer == i[1]:
        print("Sahi Zawab!!!!!!!!!!")
        amount = amount + 1000
    else:
        print("Bad luck")
        break

print("Total Amount:", amount)