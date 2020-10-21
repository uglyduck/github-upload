import numpy as np
import matplotlib.pyplot as plt
import random

def function_move(position):
	pos = position;
	
	n=random.randint(1,6)
	move=int(n)
	moved = np.array([0,0,0])

	if move == 1:
		pos_current=pos+np.array([0,1,0])
		#print ("moved UP, Current Position ",pos_current)
	if move == 2:
		pos_current=pos+np.array([0,-1,0])
		#print ("moved DOWN, Current Position ",pos_current)
	if move == 3:
		pos_current=pos+np.array([-1,0,0])
		#print ("moved LEFT, Current Position ",pos_current)
	if move == 4:
		pos_current=pos+np.array([1,0,0])
		#print ("moved RIGHT, Current Position ",pos_current)
	if move == 5:
		pos_current=pos+np.array([0,0,1])
		#print ("moved FORWARD, Current Position ",pos_current)
	if move == 6:
		pos_current=pos+np.array([0,0,-1])
		#print ("moved BACKWARD, Current Position ",pos_current)
							
	return pos_current 
	
	
j=int(1)
v=np.array([0,0,0,0,0])
#w=z


while j<=int(10):

	pos=np.array([0,0,0])
	i=int(0)
	while i<=1000:
		#print(i)
		
		y=function_move(pos);
		pos=y
		if abs(y[0]) == 10: 
			#print ("Game over, ", i, " moves");
			break
		if abs(y[1]) == 10: 
			#print ("Game over, ", i, " moves");
			break
		if abs(y[2]) == 10: 
			#print ("Game over, ", i, " moves");
			break		
		i += 1
	y=np.vstack([pos,y])
	#print (x, i, j)
	print (y)
		
	v=np.array([y[0],y[1],y[2],i,j])
	z = np.vstack([v, v])
	j += 1

z=np.delete(z,0,0)
# z=z=np.delete(arrayname,row or column no,0 or 1 for row or column)
#z[:,3]
print (z[:,3])
#print (z)
print (np.max(z[:,3]))

fig=plt.figure()
axes=plt.axes(projection="3d")
axes.set_xlabel("x")
axes.set_ylabel("y")
axes.set_zlabel("z")
line=axes.scatter3D(z[:,0],z[:,1],z[:,2],'green')


#plt.show()