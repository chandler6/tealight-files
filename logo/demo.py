from tealight.logo import (move, 
                           turn, 
                           color)

colors = ["red", "green", "blue"]

for i in range(1,100):
  move(i)
  turn(93)
      
  color(colors[i%3])