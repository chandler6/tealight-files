from tealight.art import (color, line, spot, circle, box, image, text, background)

from github.mauriceyap.art.maths_mechanism import *


turn = 1
cell_size = 100

cells_x = 8
cells_y = 8

offset_x = 20
offset_y = 80

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
  box(offset_x,offset_y,cell_size * cells_x,cell_size * cells_y)
  
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