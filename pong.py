import turtle # enables graphics for games

pong = turtle.Screen()
pong.title("Pong Game by Nurhaliza H")
pong.bgcolor("blue")
pong.setup(width = 800, height = 600)
pong.tracer(0) # stops the window from updating - speeds up game process

# paddle (a)
paddleA = turtle.Turtle()
paddleA.speed(0) # sets max animation speed
paddleA.shape("square")
paddleA.color("grey")
paddleA.penup()
# paddle (b)
