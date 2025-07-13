import random
import time
OPERATORS = ['+', '-', '*']
min_operand = 3
max_operand =20
TOTAL_PROBLEMS = 10


def generate_problem():
    left =random.randint(min_operand,max_operand)
    right=random.randint(min_operand,max_operand)
    operator = random.choice(OPERATORS)
    expr =str(left) +" "+ operator +" "+ str(right)
    answer = eval(expr)
    return expr,answer


wrong = 0
input ("Press enter to start!")
print("-------------------------")

start_time = time.time()
for  i in range(TOTAL_PROBLEMS):

      expr,answer = generate_problem()
      while True: 
         guess = input("Problem #" + str(i+1)+ ": " + expr +" = ")
         if guess == str(answer):
             break
         wrong+=1 
end_time = time.time()

total_time =int( end_time - start_time)
print("-----------------------------------")
print(f"Your total time is {total_time} seconds")
print(f"You get {wrong} wrong answer" )
