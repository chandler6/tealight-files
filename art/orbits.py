from tealight.art import (color, line, spot, circle, box, image, text, background)

x = 600
y = 50
vx = 0
vy = 0
ax = 0
ay = 0.05

power = 1

def handle_keydown(key):
  global ax, ay
  

  if key == "left":
    ax = -power
  elif key == "right":
    ax = power
  elif key == "up":
    ay = -power
  elif key == "down":
    ay = power

def handle_keyup(key):
  global ax, ay

  if key == "left" or key == "right":
    ax = 0
  elif key == "up" or key == "down":
    ay = 0
    
def handle_frame():
  global x,y,vx,vy,ax,ay
  
  color("red")
  
  spot (x,y,25)
  vx = vx + ax
  vy = vy + ay
  
  x = x + vx
  y = y + vy
  
  color("black")
  
  spot (x,y,25)
  