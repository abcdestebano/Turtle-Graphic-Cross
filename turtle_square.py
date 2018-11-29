import turtle

tortuga = turtle.Turtle()

tortuga.sety(200)

lines = [
    {
        "color": "yellow",
        "turn": 90,
        "draw": 100,
        "angle": "right",
        "to": "forward"

    },
    {
        "color": "red",
        "turn": 180,
        "draw": 250,
        "angle": "right",
        "to": "backward"
    },
    {
        "color": "brown",
        "turn": 180,
        "draw": 250,
        "angle": "left",
        "to": "backward"
    },
    {
        "color": "blue",
        "turn": 90,
        "draw": 100,
        "angle": "left",
        "to": "forward"
    },
    {
        "color": "gray",
        "turn": 180,
        "draw": 200,
        "angle": "right",
        "to": "forward"
    }
]


def setPenSize():
    tortuga.pensize(50)


def setPenColor(color):
    tortuga.pencolor(color)


def drawForward(distance):
    tortuga.forward(distance)


def drawBackward(distance):
    tortuga.backward(distance)


def turnRight(angle):
    tortuga.right(angle)


def turnLeft(angle):
    tortuga.left(angle)


setPenSize()

for line in lines:
    setPenColor(line['color'])
    if (line["angle"] == 'right'):
        turnRight(line["turn"])
    else:
        turnLeft(line["turn"])

    if (line["to"] == 'forward'):
        drawForward(line["draw"])
    else:
        drawBackward(line["draw"])

turtle.mainloop()
