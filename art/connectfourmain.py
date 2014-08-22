from tealight.art import (color, line, spot, circle, box, image, text, background)

from github.mauriceyap.art.maths_mechanism import *


turn = 0
cell_size = 100

cells_x = 8
cells_y = 8

offset_x = 200
offset_y = 80

def handle_mousedown(x,y,button):
  global turn
  
  col = (x-offset_x) / cell_size
  
  if 0 <= col < 8:
    
    drop_counter(col,turn+1)
    
    turn = (turn + 1) % 2
    
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
  
  width = 20
  height = 8
  
  for i in range(0,cells_x):
    for j in range(0,cells_y):
  
      if boardArray [j][i] == 0:
        color("white")
      elif boardArray[j][i] == 1:
        color("red")
      elif boardArray[j][i] == 2:
        color("yellow")
      
      spot(offset_x + i * cell_size + cell_size/2, offset_y + j * cell_size + cell_size/2, cell_size *0.4)

draw()