from tealight.art import (color, line, spot, circle, box, image, text, background)


def handle_mousedown(x,y,button):
  if button == "left":
    color("red")
    spot(x,y,50)
  elif button == "right":
    color("yellow")
    spot(x,y,50)
    



color("blue")
box(20,80,850,840)

x = 100
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