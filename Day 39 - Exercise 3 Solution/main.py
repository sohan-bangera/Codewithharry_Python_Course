questions = [
  [
    "Which planet is known as the Red Planet?", "Earth", "Mars", "Jupiter",
    "Venus", "Saturn", 2
  ],
  [
    "Who developed the theory of relativity?", "Newton", "Einstein", "Tesla",
    "Edison", "Bohr", 2
  ],
  [
    "Which data structure uses FIFO?", "Stack", "Queue", "Tree",
    "Graph", "Heap", 2
  ],
  [
    "Which keyword is used to define a function in Python?", "func", "define", "def",
    "function", "lambda", 3
  ],
  [
    "Which company developed Java?", "Microsoft", "Google", "Sun Microsystems",
    "Apple", "IBM", 3
  ],
  [
    "What is the capital of Japan?", "Seoul", "Beijing", "Tokyo",
    "Bangkok", "Hanoi", 3
  ],
  [
    "Which operator is used for exponent in Python?", "^", "**", "*",
    "//", "%", 2
  ],
  [
    "Which language is primarily used for web styling?", "HTML", "CSS", "JavaScript",
    "Python", "C++", 2
  ],
  [
    "Which database is relational?", "MongoDB", "MySQL", "Redis",
    "Cassandra", "DynamoDB", 2
  ],
  [
    "Which loop is guaranteed to execute at least once?", "for", "while", "do-while",
    "foreach", "loop", 3
  ],
  [
    "Which is not a programming language?", "Python", "Java", "HTML",
    "C++", "Ruby", 3
  ],
  [
    "What does CPU stand for?", "Central Process Unit", "Central Processing Unit", "Computer Personal Unit",
    "Central Power Unit", "Control Processing Unit", 2
  ],
  [
    "Which HTTP method is used to retrieve data?", "POST", "PUT", "GET",
    "DELETE", "PATCH", 3
  ],
  [
    "Which keyword is used to create a class in Java?", "class", "Class", "define",
    "struct", "object", 1
  ],
  [
    "Which is the largest ocean?", "Atlantic", "Indian", "Pacific",
    "Arctic", "Southern", 3
  ],
]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 5000000, 10000000]
money = 0
for i in range(0, len(questions)):
    question = questions[i]
    print(f"Question for Rs. {levels[i]}")
    print(question[0])
    print(f"a. {question[1]}       b. {question[2]}")
    print(f"c. {question[3]}       c. {question[4]}")
    reply = int(input("Enter the answer in the form of 1,2,3,4:"))
    if(i == 4):
        money = 10000
    elif(i == 9):
        money = 320000
    elif(i == 14):
        money = 10000000
    if(reply == question[-1]):
        print(f"Correct answer, you have won {levels[i]}")
    else:
        print(f"Wrong Answer!")
        break
print(f"You have won {money}")