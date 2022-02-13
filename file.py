import turtle
import random


a = 50
b = 50
c = 50
d = 50
while True:




    turtle.rt(c)
    turtle.left(d)
    turtle.fd(a)
    turtle_position = turtle.pos()
    print(turtle_position)
    turtle_ud_position = turtle_position[0]
    turtle_rl_position = turtle_position[1]
    if turtle_ud_position >= 400 or turtle_ud_position <= -400 or turtle_rl_position >= 400 or turtle_rl_position <= -400:
        print('active')
        turtle.back(a)
    '''turtle.back(b)
    turtle_position = turtle.pos()
    print(turtle_position)
    turtle_ud_position = turtle_position[0]
    turtle_rl_position = turtle_position[1]
    if turtle_ud_position >= 400 or turtle_ud_position <= -400 or turtle_rl_position >= 400 or turtle_ud_position <= -400:
        turtle.fd(a)'''


    a = random.randint(0,100)
    b = random.randint(0,100)
    c = random.randint(0,100)
    d = random.randint(0,100)

    #if turtle_ud_position >= 400 or turtle_ud_position <= 0 or turtle_rl_position >= 400 or turtle_ud_position <= 400:
