from tealight.art import (color, line, spot, circle, box, image, text, background)
turn = 1
if def handle_mousedown(x,y,button):
  turn = 2
def handle_mousedown(x,y,button):
  if button == "left":
    color("red")
    spot(x,y,40)
  elif button == "right":
    color("yellow")
    spot(x,y,40)