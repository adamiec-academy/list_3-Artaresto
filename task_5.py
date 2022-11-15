from turtle import forward, left, right, speed, penup, pendown, exitonclick, pos, heading, setposition, setheading 


speed("fast")
def square_star(arms_number, arms_lenght):
    for _ in range(arms_number):
        left(180)
        forward(40)
        starting_pos_base = pos()
        right(90)
        
        for square_circuit in range(arms_lenght):
            circuit = arms_lenght * (square_circuit + 1)
            side = 40 - circuit
            forward(side)
            right(90)
            forward(arms_lenght/2)
            starting_pos_arms = pos()
            starting_heading_arms = heading()
            forward(arms_lenght/2)
            forward(side)
            right(90)
            forward(side)
            penup()
            setposition(starting_pos_arms)
            setheading(starting_heading_arms)
            pendown()
            left(90)
        
        penup()
        setposition(starting_pos_base)
        pendown()
        
        right((360/arms_number/2))

    exitonclick()
