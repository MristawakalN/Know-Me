#Python Countdown timer
import time
import turtle
import socket
a = socket.gethostname()
b = socket.getbyhostname(a)
aku = b
def countdown(time_sec):
    while time_sec:
        mins, secs = divmod (time_sec, 60)
        timeformat = '{:02d}:{:02d}'.format(mins,secs)
        print(timeformat, end='\r')
        time.sleep(1)
        time_sec -= 1
    print("Time Ended !")
countdown (5)
screen = turtle. Screen ()
screen.setup(500, 600, startx=0, starty=100)
t = turtle.Turtle()
s = turtle. Screen ()
s.bgcolor("black")
t. pencolor("red")
a = 0
b = 0
t.speed (0)
t. penup()
t.goto(0,200)
t. pendown ()
while(True):
    t. forward (a)
    t.right(b)
    a+=3
    b+=1
    if b == 210:
        break
    t.hideturtle()

turtle.done()
