"""
Draws Super Heroes using Turtle
"""

from turtle import *
screen = Screen()
turtle01 = Turtle()
turtle02 = Turtle()
turtle03 = Turtle()
turtle04 = Turtle()
turtle05 = Turtle()
turtle06 = Turtle()
turtle07 = Turtle()
turtle08 = Turtle()
turtle09 = Turtle()
turtle10 = Turtle()
turtle11 = Turtle()
turtle12 = Turtle()
turtle13 = Turtle()
turtle14 = Turtle()
turtle15 = Turtle()
turtle16 = Turtle()
turtle17 = Turtle()
turtle18 = Turtle()
turtle19 = Turtle()
turtle20 = Turtle()
turtle21 = Turtle()
turtle22 = Turtle()
turtle23 = Turtle()
turtle24 = Turtle()
turtle25 = Turtle()
turtle26 = Turtle()
turtle27 = Turtle()
turtle28 = Turtle()
turtle29 = Turtle()
turtle30 = Turtle()
turtle31 = Turtle()
turtle32 = Turtle()
turtle33 = Turtle()
turtle34 = Turtle()

"""
Draws Iron Man aka the greatest superhero of all time.
"""
def drawIronMan(numOfSquares):

    turtle01.penup()
    turtle01.goto(-250, 285)
    turtle01.pendown()

    turtle02.penup()
    turtle02.goto(-250, 270)
    turtle02.pendown()

    turtle03.penup()
    turtle03.goto(-250, 255)
    turtle03.pendown()

    turtle04.penup()
    turtle04.goto(-250, 240)
    turtle04.pendown()

    turtle05.penup()
    turtle05.goto(-250, 225)
    turtle05.pendown()

    turtle06.penup()
    turtle06.goto(-250, 210)
    turtle06.pendown()

    turtle07.penup()
    turtle07.goto(-250, 195)
    turtle07.pendown()

    turtle08.penup()
    turtle08.goto(-250, 180)
    turtle08.pendown()

    turtle09.penup()
    turtle09.goto(-250, 165)
    turtle09.pendown()

    turtle10.penup()
    turtle10.goto(-250, 150)
    turtle10.pendown()

    turtle11.penup()
    turtle11.goto(-250, 135)
    turtle11.pendown()

    turtle12.penup()
    turtle12.goto(-250, 120)
    turtle12.pendown()

    turtle13.penup()
    turtle13.goto(-250, 105)
    turtle13.pendown()

    turtle14.penup()
    turtle14.goto(-250, 90)
    turtle14.pendown()

    turtle15.penup()
    turtle15.goto(-250, 75)
    turtle15.pendown()

    turtle16.penup()
    turtle16.goto(-250, 60)
    turtle16.pendown()

    turtle17.penup()
    turtle17.goto(-250, 45)
    turtle17.pendown()

    turtle18.penup()
    turtle18.goto(-250, 30)
    turtle18.pendown()

    turtle19.penup()
    turtle19.goto(-250, 15)
    turtle19.pendown()

    turtle20.penup()
    turtle20.goto(-250, 0)
    turtle20.pendown()

    turtle21.penup()
    turtle21.goto(-250, -15)
    turtle21.pendown()

    turtle22.penup()
    turtle22.goto(-250, -30)
    turtle22.pendown()

    turtle23.penup()
    turtle23.goto(-250, -45)
    turtle23.pendown()

    turtle24.penup()
    turtle24.goto(-250, -60)
    turtle24.pendown()

    turtle25.penup()
    turtle25.goto(-250, -75)
    turtle25.pendown()

    turtle26.penup()
    turtle26.goto(-250, -90)
    turtle26.pendown()

    turtle27.penup()
    turtle27.goto(-250, -105)
    turtle27.pendown()

    turtle28.penup()
    turtle28.goto(-250, -120)
    turtle28.pendown()

    turtle29.penup()
    turtle29.goto(-250, -135)
    turtle29.pendown()

    turtle30.penup()
    turtle30.goto(-250, -150)
    turtle30.pendown()

    turtle31.penup()
    turtle31.goto(-250, -165)
    turtle31.pendown()

    turtle32.penup()
    turtle32.goto(-250, -180)
    turtle32.pendown()

    turtle33.penup()
    turtle33.goto(-250, -195)
    turtle33.pendown()

    turtle34.penup()
    turtle34.goto(-250, -210)
    turtle34.pendown()

    for i in range(numOfSquares):
        turtle01.begin_fill()
        turtle02.begin_fill()
        turtle03.begin_fill()
        turtle04.begin_fill()
        turtle05.begin_fill()
        turtle06.begin_fill()
        turtle07.begin_fill()
        turtle08.begin_fill()
        turtle09.begin_fill()
        turtle10.begin_fill()
        turtle11.begin_fill()
        turtle12.begin_fill()
        turtle13.begin_fill()
        turtle14.begin_fill()
        turtle15.begin_fill()
        turtle16.begin_fill()
        turtle17.begin_fill()
        turtle18.begin_fill()
        turtle19.begin_fill()
        turtle20.begin_fill()
        turtle21.begin_fill()
        turtle22.begin_fill()
        turtle23.begin_fill()
        turtle24.begin_fill()
        turtle25.begin_fill()
        turtle26.begin_fill()
        turtle27.begin_fill()
        turtle28.begin_fill()
        turtle29.begin_fill()
        turtle30.begin_fill()
        turtle31.begin_fill()
        turtle32.begin_fill()
        turtle33.begin_fill()
        turtle34.begin_fill()
        if i == 6:
            turtle25.fillcolor('black')
            turtle27.fillcolor('white')
            turtle29.fillcolor('white')
        elif i == 7:
            turtle18.fillcolor('black')
            turtle19.fillcolor('black')
            turtle20.fillcolor('black')
            turtle21.fillcolor('black')
            turtle23.fillcolor('black')
            turtle24.fillcolor('black')
            turtle25.fillcolor('red')
            turtle26.fillcolor('white')
            turtle27.fillcolor('white')
            turtle28.fillcolor('white')
            turtle30.fillcolor('white')


        elif i == 8:
            turtle17.fillcolor('black')
            turtle18.fillcolor('red')
            turtle19.fillcolor('red')
            turtle20.fillcolor('red')
            turtle21.fillcolor('red')

        elif i == 9:
            turtle16.fillcolor('black')


        elif i == 10:
            turtle05.fillcolor('black')
            turtle06.fillcolor('black')
            turtle07.fillcolor('black')
            turtle08.fillcolor('black')
            turtle09.fillcolor('black')
            turtle10.fillcolor('black')
            turtle11.fillcolor('black')
            turtle13.fillcolor('black')

        elif i == 11:
            turtle04.fillcolor('black')

        elif i == 12:
            turtle03.fillcolor('black')

        elif i == 13:
            turtle03.fillcolor('black')

        elif i == 14:
            turtle02.fillcolor('black')
            turtle03.fillcolor('red')

        elif i == 15:
            turtle02.fillcolor('black')
            turtle03.fillcolor('red')

        elif i == 16:
            turtle02.fillcolor('black')
            turtle03.fillcolor('red')

        elif i == 17:
            turtle02.fillcolor('black')
            turtle03.fillcolor('red')

        elif i == 18:
            turtle02.fillcolor('black')
            turtle03.fillcolor('red')
        
        elif i == 19:
            turtle03.fillcolor('black')
            turtle03.fillcolor('black')

        #elif i == 20:
        
        #elif i == 21:
        
        elif i == 22:
            turtle05.fillcolor('black')
            turtle06.fillcolor('black')
            turtle07.fillcolor('black')
            turtle08.fillcolor('black')
            turtle09.fillcolor('black')
            turtle10.fillcolor('black')
            turtle11.fillcolor('black')
            turtle13.fillcolor('black')
        
        #elif i == 23:
        
        #elif i == 24:

        #elif i == 25:

        #elif i == 26:

        #elif i == 27:

        else:
            turtle01.fillcolor('purple')
            turtle02.fillcolor('purple')
            turtle03.fillcolor('purple')
            turtle04.fillcolor('purple')

        for i in [0, 1, 2, 3]:
            turtle01.forward(15)
            turtle02.forward(15)
            turtle03.forward(15)
            turtle04.forward(15)
            turtle05.forward(15)
            turtle06.forward(15)
            turtle07.forward(15)
            turtle08.forward(15)
            turtle09.forward(15)
            turtle10.forward(15)
            turtle11.forward(15)
            turtle12.forward(15)
            turtle13.forward(15)
            turtle14.forward(15)
            turtle15.forward(15)
            turtle16.forward(15)
            turtle17.forward(15)
            turtle18.forward(15)
            turtle19.forward(15)
            turtle20.forward(15)
            turtle21.forward(15)
            turtle22.forward(15)
            turtle23.forward(15)
            turtle24.forward(15)
            turtle25.forward(15)
            turtle26.forward(15)
            turtle27.forward(15)
            turtle28.forward(15)
            turtle29.forward(15)
            turtle30.forward(15)
            turtle31.forward(15)
            turtle32.forward(15)
            turtle33.forward(15)
            turtle34.forward(15)    
            turtle01.left(90)
            turtle02.left(90)
            turtle03.left(90)
            turtle04.left(90)
            turtle05.left(90)
            turtle06.left(90)
            turtle07.left(90)
            turtle08.left(90)
            turtle09.left(90)
            turtle10.left(90)
            turtle11.left(90)
            turtle12.left(90)
            turtle13.left(90)
            turtle14.left(90)
            turtle15.left(90)
            turtle16.left(90)
            turtle17.left(90)
            turtle18.left(90)
            turtle19.left(90)
            turtle20.left(90)
            turtle21.left(90)
            turtle22.left(90)
            turtle23.left(90)
            turtle24.left(90)
            turtle25.left(90)
            turtle26.left(90)
            turtle27.left(90)
            turtle28.left(90)
            turtle29.left(90)
            turtle30.left(90)
            turtle31.left(90)
            turtle32.left(90)
            turtle33.left(90)
            turtle34.left(90)
        turtle01.begin_fill()
        turtle02.begin_fill()
        turtle03.begin_fill()
        turtle04.begin_fill()
        turtle05.begin_fill()
        turtle06.begin_fill()
        turtle07.begin_fill()
        turtle08.begin_fill()
        turtle09.begin_fill()
        turtle10.begin_fill()
        turtle11.begin_fill()
        turtle12.begin_fill()
        turtle13.begin_fill()
        turtle14.begin_fill()
        turtle15.begin_fill()
        turtle16.begin_fill()
        turtle17.begin_fill()
        turtle18.begin_fill()
        turtle19.begin_fill()
        turtle20.begin_fill()
        turtle21.begin_fill()
        turtle22.begin_fill()
        turtle23.begin_fill()
        turtle24.begin_fill()
        turtle25.begin_fill()
        turtle26.begin_fill()
        turtle27.begin_fill()
        turtle28.begin_fill()
        turtle29.begin_fill()
        turtle30.begin_fill()
        turtle31.begin_fill()
        turtle32.begin_fill()
        turtle33.begin_fill()
        turtle34.begin_fill()
        turtle01.fillcolor('purple')
        turtle02.fillcolor('purple')
        turtle03.fillcolor('purple')
        turtle04.fillcolor('purple')
        turtle05.fillcolor('purple')
        turtle06.fillcolor('purple')
        turtle07.fillcolor('purple')
        turtle08.fillcolor('purple')
        turtle09.fillcolor('purple')
        turtle10.fillcolor('purple')
        turtle11.fillcolor('purple')
        turtle12.fillcolor('purple')
        turtle13.fillcolor('purple')
        turtle14.fillcolor('purple')
        turtle15.fillcolor('purple')
        turtle16.fillcolor('purple')
        turtle17.fillcolor('purple')
        turtle18.fillcolor('purple')
        turtle19.fillcolor('purple')
        turtle20.fillcolor('purple')
        turtle21.fillcolor('purple')
        turtle22.fillcolor('purple')
        turtle23.fillcolor('purple')
        turtle24.fillcolor('purple')
        turtle25.fillcolor('purple')
        turtle26.fillcolor('purple')
        turtle27.fillcolor('purple')
        turtle28.fillcolor('purple')
        turtle29.fillcolor('purple')
        turtle30.fillcolor('purple')
        turtle31.fillcolor('purple')
        turtle32.fillcolor('purple')
        turtle33.fillcolor('purple')
        turtle34.fillcolor('purple')
        turtle01.forward(15)
        turtle02.forward(15)
        turtle03.forward(15)
        turtle04.forward(15)
        turtle05.forward(15)
        turtle06.forward(15)
        turtle07.forward(15)
        turtle08.forward(15)
        turtle09.forward(15)
        turtle10.forward(15)
        turtle11.forward(15)
        turtle12.forward(15)
        turtle13.forward(15)
        turtle14.forward(15)
        turtle15.forward(15)
        turtle16.forward(15)
        turtle17.forward(15)
        turtle18.forward(15)
        turtle19.forward(15)
        turtle20.forward(15)
        turtle21.forward(15)
        turtle22.forward(15)
        turtle23.forward(15)
        turtle24.forward(15)
        turtle25.forward(15)
        turtle26.forward(15)
        turtle27.forward(15)
        turtle28.forward(15)
        turtle29.forward(15)
        turtle30.forward(15)
        turtle31.forward(15)
        turtle32.forward(15)
        turtle33.forward(15)
        turtle34.forward(15)
        turtle01.end_fill()
        turtle02.end_fill()
        turtle03.end_fill()
        turtle04.end_fill()
        turtle05.end_fill()
        turtle06.end_fill()
        turtle07.end_fill()
        turtle08.end_fill()
        turtle09.end_fill()
        turtle10.end_fill()
        turtle11.end_fill()
        turtle12.end_fill()
        turtle13.end_fill()
        turtle14.end_fill()
        turtle15.end_fill()
        turtle16.end_fill()
        turtle17.end_fill()
        turtle18.end_fill()
        turtle19.end_fill()
        turtle20.end_fill()
        turtle21.end_fill()
        turtle22.end_fill()
        turtle23.end_fill()
        turtle24.end_fill()
        turtle25.end_fill()
        turtle26.end_fill()
        turtle27.end_fill()
        turtle28.end_fill()
        turtle29.end_fill()
        turtle30.end_fill()
        turtle31.end_fill()
        turtle32.end_fill()
        turtle33.end_fill()
        turtle34.end_fill()
    turtle01.penup()
    turtle02.penup()
    turtle03.penup()
    turtle04.penup()
    turtle05.penup()
    turtle06.penup()
    turtle07.penup()
    turtle08.penup()
    turtle09.penup()
    turtle10.penup()
    turtle11.penup()
    turtle12.penup()
    turtle13.penup()
    turtle14.penup()
    turtle15.penup()
    turtle16.penup()
    turtle17.penup()
    turtle18.penup()
    turtle19.penup()
    turtle20.penup()
    turtle21.penup()
    turtle22.penup()
    turtle23.penup()
    turtle24.penup()
    turtle25.penup()
    turtle26.penup()
    turtle27.penup()
    turtle28.penup()
    turtle29.penup()
    turtle30.penup()
    turtle31.penup()
    turtle32.penup()
    turtle33.penup()
    turtle34.penup()

"""
My main bitch.
"""
def main():   
    screen.title('Drawing Super Heroes!') # Put label on top of page
    turtle01.hideturtle()
    turtle02.hideturtle()
    turtle03.hideturtle()
    turtle04.hideturtle()
    turtle05.hideturtle()
    turtle06.hideturtle()
    turtle07.hideturtle()
    turtle08.hideturtle()
    turtle09.hideturtle()
    turtle10.hideturtle()
    turtle11.hideturtle()
    turtle12.hideturtle()
    turtle13.hideturtle()
    turtle14.hideturtle()
    turtle15.hideturtle()
    turtle16.hideturtle()
    turtle17.hideturtle()
    turtle18.hideturtle()
    turtle19.hideturtle()
    turtle20.hideturtle()
    turtle21.hideturtle()
    turtle22.hideturtle()
    turtle23.hideturtle()
    turtle24.hideturtle()
    turtle25.hideturtle()
    turtle26.hideturtle()
    turtle27.hideturtle()
    turtle28.hideturtle()
    turtle29.hideturtle()
    turtle30.hideturtle()
    turtle31.hideturtle()
    turtle32.hideturtle()
    turtle33.hideturtle()
    turtle34.hideturtle()
    turtle01.speed(0)
    turtle02.speed(0)
    turtle03.speed(0)
    turtle04.speed(0)
    turtle05.speed(0)
    turtle06.speed(0)
    turtle07.speed(0)
    turtle08.speed(0)
    turtle09.speed(0)
    turtle10.speed(0)
    turtle11.speed(0)
    turtle12.speed(0)
    turtle13.speed(0)
    turtle14.speed(0)
    turtle15.speed(0)
    turtle16.speed(0)
    turtle17.speed(0)
    turtle18.speed(0)
    turtle19.speed(0)
    turtle20.speed(0)
    turtle21.speed(0)
    turtle22.speed(0)
    turtle23.speed(0)
    turtle24.speed(0)
    turtle25.speed(0)
    turtle26.speed(0)
    turtle27.speed(0)
    turtle28.speed(0)
    turtle29.speed(0)
    turtle30.speed(0)
    turtle31.speed(0)
    turtle32.speed(0)
    turtle33.speed(0)
    turtle34.speed(0)

    screen.setup(500, 600) # Set up the screen size
    drawIronMan(34)
    screen.exitonclick()

main()
