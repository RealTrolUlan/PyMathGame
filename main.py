import random
import time

OPERATORS = ["+", "-", "/","*"]
MIN_OPERAND = 3
MAX_OPERAND = 10
TOTAL_PROBLEMS = input("How many problems would you like to generate? \n")


def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)

    expr = str(left) + " " +  str(operator) + " " + str(right)
    answer = eval(expr)
    return expr, answer

wrong = 0
input("press any key to start!")
print("------------------------")

start_time = time.time()

for i in range(int(TOTAL_PROBLEMS)):
    expr, answer = generate_problem()
    while True:
        guess = input("Problem #" + str(i * i) + ": " + expr + " = ")
        if guess == str(answer):
            break
        wrong += 1

end_time = time.time()
total_time = round(end_time - start_time, 4)


print("----------------------------")
print("Great job! You finished in ", total_time, " seconds")
