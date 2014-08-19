from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)



while left_side()=='wall':
  move()
  if touch()=='wall':
   turn(-1)
if touch()=='wall':
  turn(2)
while left_side()=='wall':
  move()
  if touch()=='wall':
   turn(-1)
while right_side()=='wall':
  move()
  if touch() =='wall':
    turn(1)
while left_side()=='wall':
  move()