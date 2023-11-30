import turtle

def draw_rectangle(color, width, height):
    turtle.begin_fill()
    turtle.fillcolor(color)
    for _ in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)
    turtle.end_fill()

def draw_isosceles_triangle(color, base, height):
    turtle.begin_fill()
    turtle.fillcolor(color)

    # Drawing the isosceles triangle
    turtle.forward(base / 2)
    turtle.left(120)
    turtle.forward(base / 2)
    turtle.left(120)
    turtle.forward(base / 2)

    turtle.end_fill()

# Set up the turtle
turtle.speed(2)
turtle.hideturtle()

# Draw the green background
draw_rectangle("#138808", 300, 150)  # Adjusted for height=150, length=300

# Draw the yellow cross
turtle.penup()
turtle.goto(-50, -75)  # Adjusted for the new height
turtle.pendown()
draw_rectangle("#fcd116", 100, 30)

turtle.penup()
turtle.goto(-50, -60)  # Adjusted for the new height
turtle.pendown()
draw_rectangle("#fcd116", 30, 100)

# Draw the green isosceles triangle at the top
turtle.penup()
turtle.goto(-50, 75)  # Position at the top
turtle.pendown()
draw_isosceles_triangle("#138808", 120, 60)  # Adjust the base and height as needed

# Close the window on click
turtle.exitonclick()
