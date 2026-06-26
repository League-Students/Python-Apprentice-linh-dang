import turtle 

tina = turtle.Turtle()

tina.shape("turtle")

screen = turtle.Screen()

def move_forward():
  tina.forward(20)
  
screen.listen()
screen.onkey(move_forward, "Up")
