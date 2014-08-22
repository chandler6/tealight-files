from tealight.art import (color, line, spot, circle, box, image, text, background)

from github.mauriceyap.art.maths_mechanism import *

print boardArray

turn = 1

def handle_mousedown(x,y,button):
  global turn
  
  
  
  draw()
  
  #if button == "left" and turn == 1:
  #  color("red")
  #  spot(x,y,40)
  #  
  #  turn = 2
  #elif button == "right"and turn == 2:
  #  color("yellow")
  #  spot(x,y,40)
  #  turn = 1
    
    
    


      
def draw():
  color("blue")
  box(20,80,850,840)
  
  x = 95
  y =150
  
  width = 20
  height = 8
  
  for i in range(0,8):
    for j in range(0,8):
  
      if boardArray [j][i] == 0:
        color("white")
      elif boardArray[j][i] == 1:
        color("red")
      elif boardArray[j][i] == 2:
        color("yellow")
      
      spot(x + i * 100, y + j * 100, 40)

draw()