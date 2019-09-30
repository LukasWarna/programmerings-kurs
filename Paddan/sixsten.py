open = True

import turtle            
sixsten = turtle.Turtle()
sixsten.speed(50)
sixsten.penup()


while open:
    planX = input("Var vill du ha pricken på plan X?")
    
    planY = input("Var vill du ha pricken på plan Y?")
   
    sixsten.goto(int(planX), int(planY))
    sixsten.pendown()
    sixsten.dot()

    sixsten.penup()


a = input()
