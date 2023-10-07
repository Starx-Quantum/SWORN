import turtle
t = turtle.Turtle()

screen = turtle.Screen()
screen.setup(width = 1.0, height = 1.0)
   
def curve():
    for i in range(200):
      t.right(1)
      t.forward(8)
    
    t.fillcolor("green")
    t.begin_fill()
    t.circle(50)
    t.end_fill()
    
    t.penup()
    t.setpos(1000, 0)
    t.pendown()
    
    t.fillcolor("black")
    t.begin_fill()
    t.circle(50)
    t.end_fill()
    
    t.left(90)
    t.forward(250)
    
    t.fillcolor("brown")
    t.begin_fill()
    t.circle(50)
    t.end_fill()
    
    t.fillcolor("black")
    t.begin_fill()
    t.left(90)
    t.forward(100)
    
    t.left(90)
    t.forward(200)
    
    t.left(90)
    t.forward(100)
    t.end_fill()
    
    t.backward(55)
    t.left(90)
    t.forward(250)
    
    t.color("Brown")
    t.pensize(5)
    
    curve()
    
    turtle.done()
    
    
    
    
    
    
    
                
            
