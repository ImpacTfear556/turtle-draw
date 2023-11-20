# TurtleDraw
# By: Angelo Fornero


import turtle

TEXTFILENAME = 'turtle-text.txt'

# Todo: Ask user for the file name. 



turtleScreen = turtle.Screen()
turtleScreen.setup(450, 450)

turtleDraw = turtle.Turtle()
turtleDraw.speed(10)
turtleDraw.penup()

turtleDrawTextfile = open(TEXTFILENAME, 'r')
line = turtleDrawTextfile.readline()
while line:
	print(line, end='')
	parts = line.split(' ')

	if (len(parts) == 3):
		color = parts[0]
		x = int(parts[1])
		y = int(parts[2])

		turtleDraw.color(color)
		turtleDraw.goto(x,y)

		# Todo: Calculate the distance and add it to the total distance.)


		turtleDraw.pendown()

	if (len(parts) == 1): 
		turtleDraw.penup()

	line = turtleDrawTextfile.readline()

# Todo: Print the total near the bottom. 

turtle.done()
turtleDrawTextfile.close()

# Todo: Wait for the user to press the enter key before closing. 

print('\nEnd')
