import numpy as np
import random

pos_init=np.array([1,1,1])
pos = pos_init;
print ("Initial Position ", pos)

move_up = np.array([0,1,0])
move_down = np.array([0,-1,0])
move_left = np.array([-1,0,0])
move_right = np.array([1,0,0])
move_fw = np.array([0,0,1])
move_bw = np.array([0,0,-1])

n=random.randint(1,6)
move=int(n)
moved = np.array([0,0,0])
#moved = move_up;
if move == 1:
	moved = move_up;
	print ("moved UP",moved)
if move == 2: 
	moved = move_down;
	print ("moved DOWN",moved)
if move == 3:
	moved = move_left;
	print ("moved LEFT",moved)
if move == 4:
	moved =move_right;
	print ("moved RIGHT",moved)
if move == 5:
	moved = move_fw;
	print ("moved FORWARD",moved)
if move == 6:
	moved = move_bw;
	print ("moved BACKWARD",moved)
#	else: 
#		moved = np.array([0,0,0]);

pos_new=pos+moved
print ("move ",move," Current position ",pos_new)

return pos_new