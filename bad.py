
import numpy as np

x=0;
y=0;
z=0;
pos_init=np.array([x,y,z])
pos = pos_init;

move_up = np.array([0,1,0])
move_down = np.array([0,-1,0])
move_left = np.array([-1,0,0])
move_right = np.array([1,0,0])
move_fw = np.array([0,0,1])
move_bw = np.array([0,0,-1])

move=2,
moved = np.array([0,0,0])
moved = move_up;
if move == 1:
	moved = move_up;
	print ("move1",moved)
if move == 2: 
	moved = move_down;
	print ("move2",moved)
if move == 3:
	moved = move_left;
	print ("move3",moved)
if move == 4:
	moved =move_right;
	print ("move4",moved)
if move == 5:
	moved = move_fw;
	print ("move5",moved)
if move == 6:
	moved = move_bw;
	print ("move6",moved)
#	else: 
#		moved = np.array([0,0,0]);

print (move,moved)



