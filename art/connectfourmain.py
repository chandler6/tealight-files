from tealight.art import (color, line, spot, circle, box, image, text, background)

#1The board

boardArray =[[0,0,0,0,0,0,0,0],
             [0,1,0,0,0,0,0,1],
             [0,0,1,0,0,0,1,0],
             [0,0,0,1,0,1,0,0],
             [0,0,0,0,1,2,2,2],
             [0,0,0,1,0,0,0,0],
             [0,0,1,0,0,0,0,0],
             [0,0,0,0,0,0,0,0]]

turn = 1

y = 10

def handle_mousedown(x,y,button):
  global turn
  if button == "left" and turn == 1:
    color("red")
    y = y + vy
    vy = vy + ay +0.12
    spot(x,y,50)
    turn = 2
  elif button == "right"and turn == 2:
    color("yellow")
    spot(x,y,50)
    turn = 1
    



color("blue")
box(20,80,850,840)

x = 95
y =150

width = 20
height = 8

for i in range(0,8):
  for j in range(0,8):
    if (i + j)%4 ==0:
      color("white")
      spot(x + i * 100, y + j * 100, 40)
    else:
      spot(x + i * 100, y + j * 100, 40)