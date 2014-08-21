from tealight.art import (color, line, spot, circle, box, image, text, background)
from tealight.art import (screen_width, screen_height)

x = 600
y = 400
vx = 0
vy = 0
ax = 0
ay = 0

def handle_mousedown(x,y,button):
  if button == "left":
   
   color("white")
  
   spot(x,y,8)
   x = 10 
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
  
 

  
  
    