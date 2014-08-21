from tealight.art import (color, line, spot, circle, box, image, text, background)
from tealight.art import (screen_width, screen_height)



def handle_frame():
  global x,y,vx,vy,ax,ay
  
  color("white")
  
  spot(x,y,8)
 
  vx = (vx+ax)*0.97
  vy = vy + ay +0.12
  if vy > 10:
    vy =10
  
  x = x + vx
  y = y + vy
  if y >= 800:
    vy=-1*abs(0.4*vy)
    if y>805:
      y=805
  
  color("blue")
  
  spot(x,y,8)
