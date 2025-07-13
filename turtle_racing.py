import turtle
import time
import random 
WIDTH, HEIGHT = 500, 500
COLORS =['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink', 'black' , 'gray', 'brown', 'olive','violet']

def get_number_of_racers():
    racers =0
    while True:
        racers =input("Enter the number of racers (2-10): ")
        if racers.isdigit():
            racers=int(racers)
            if 2 <= racers <=10:
                break
            else:
                print("Must be between 2 and 10 racers")   
        else:
            print("Ivalid number of racers")
    return racers

def race(colors):
    turtles = create_turtles(colors)
    while True:
        for racer in turtles:
            racer.forward(random.randint(1,10))
            x,y = racer.pos()
            if y >= HEIGHT//2-10:
                return colors[turtles.index(racer)]
            

def create_turtles(colors):
    turtles= []
    for i,color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape("turtle")
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2 +(i+1)*(WIDTH//number_of_racers), -HEIGHT//2+20)
        racer.pendown()
        turtles.append(racer)
    return turtles


def init_turtles():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle Racing Game")


def bet(colors):
    print("So this will be 50/50 bet ether you win double or you lose all: ")
    while True:
       bet_amount =input("Enter the amount you want to bet: ")
       if bet_amount.isdigit():
            bet_amount =int(bet_amount)
            bet_color = input(f"Enter the color you want to bet on{colors}: ")
            return bet_amount, bet_color
       else:
            print("Invalid input")     


number_of_racers =get_number_of_racers()
win_amount =0
init_turtles()
random.shuffle(COLORS)
colors =COLORS[:number_of_racers]
bet_amount, bet_color = bet(colors)
winner = race(colors)
print(f"The winner is {winner}")
time.sleep(3)
if winner == bet_color:
    win_amount = bet_amount*2
    print(f"You won {win_amount} dollars")
else:
    print(f"You lost all your money")    
