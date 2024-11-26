import turtle
def draw_square():
    """ draw square for turtles """
    brad = turtle.Turtle()
    brad.forward(100)  
    brad.right(90)  
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
window = turtle.Screen()
window.bgcolor("red") 
draw_square()