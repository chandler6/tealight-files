import ("color", "spot")

def handle_mousedown(x,y,button):
  if button == "left":
    color("red")
    spot(x,y,40)
  elif button == "right":
    color("yellow")
    spot(x,y,40)