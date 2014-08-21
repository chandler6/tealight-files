from tealight.art import (color, line, spot, circle, box, image, text, background)

x = 600
y = 400
vx = 0
vy = 0
ax = 0
ay = 0

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

def handle_mousedown(x,y,button):
  global turn
  if button == "left" and turn == 1:
    color("red")
    spot(x,y,50)
    
    turn = 2
  elif button == "right"and turn == 2:
    color("yellow")
    spot(x,y,50)
    turn = 1
    
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