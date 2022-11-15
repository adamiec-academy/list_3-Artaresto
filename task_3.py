from turtle import *
import random

speed ("slow")

your_highness = [5, 30, 65, 95, 125, 220, 145, 130, 90, 0, 0, 20, 50, 130, 20, 20, 0]

starting_pos = pos()
starting_heading = heading()
left(180)
forward(30)
setposition(starting_pos)
setheading(starting_heading)
forward(len(your_highness)*30)
setposition(starting_pos)
setheading(starting_heading)

for i in range(len(your_highness)):
    randomik = random.randint(-30, 30)
    if randomik < 0 or i == (len(your_highness)-1):
        goto(i * 30, your_highness[i])
    else:
        goto(i * 30, your_highness[i] + randomik)



exitonclick()
