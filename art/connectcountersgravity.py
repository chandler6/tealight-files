x = 600
y = 400
vx = 0
vy = 0
ax = 0
ay = 0
# parity = ((abs(vx + ax))/(vx + ax))

power = 0.3

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
  
  color("white")
  
  spot(x,y,8)
  image(x,y,"food/Orange.png")
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


background("paper.jpg")

line(0,813,screen_width, 813)
image(x,y,"food/Orange.png")