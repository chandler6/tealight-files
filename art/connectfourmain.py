from tealight.art import (color, line, spot, circle, box, image, text, background)


def handle_mousedown(x,y,button):
  global turn
  if button == "left" and turn == 1
    color("red")
    spot(x,y,50)
    turn = 2
  elif button == "right"and turn == 2
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