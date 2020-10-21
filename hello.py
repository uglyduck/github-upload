
import numpy as np

x=0;
y=0;
z=0;
pos_init=np.array([0,0,0])
pos = pos_init;
#pos= pos+np.array([1,1,1])
move=3,
move_up = np.array([0,1,0])
move_down = np.array([0,-1,0])
move_left = np.array([-1,0,0])
move_right = np.array([1,0,0])
move_fw = np.array([0,0,1])
move_bw = np.array([0,0,-1])

moved=np.array([0,0,0])

if move == 1: moved=move_up
if move == 2: moved=move_down
if move == 3: moved=move_left
if move == 4: moved=move_right
if move == 5: moved=move_fw
if move == 6: moved=move_bw

X=pos;
Y=moved;


# iterate through rows
#for i in range(len(X)):
   # iterate through columns
 #  for j in range(len(X[0])):
 #      result[i][j] = X[i][j] + Y[i][j]

#pos_new=result;

print("New position=",X+Y)
print("move=",pos)


