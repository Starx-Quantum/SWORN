import turtle

# Initialize the turtle and screen
t = turtle.Turtle()
screen = turtle.Screen()
screen.setup(width=1.0, height=1.0)

# Define a function to draw a curve
def curve():
    for i in range(200):
        t.right(1)
        t.forward(2)  # Decreased the forward distance for a smoother curve

    t.fillcolor("black")
    t.begin_fill()
    t.circle(50)
    t.end_fill()

# Set initial position and angle
t.penup()
t.setpos(100, 0)
t.pendown()

# Draw the first circle
t.fillcolor("black")
t.begin_fill()
t.circle(50)
t.end_fill()

# Move to the next position
t.left(90)
t.forward(250)

# Draw a brown circle
t.fillcolor("brown")
t.begin_fill()
t.circle(50)
t.end_fill()

# Draw a rectangle
t.fillcolor("black")
t.begin_fill()
t.left(90)
t.forward(100)
t.left(90)
t.forward(200)
t.left(90)
t.forward(100)
t.end_fill()

# Move to the next position
t.backward(45)
t.left(90)
t.forward(250)

# Set pen color and size
t.color("brown")
t.pensize(5)

# Draw a curve
curve()

# Finish drawing
turtle.done()
