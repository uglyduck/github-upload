import numpy as np
import matplotlib.pyplot as plt
import random

def move(position):
	pos = position;
	
	n=random.randint(1,6)
	move=int(n)
	#moved = np.array([0,0,0])

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
	#else: pos_current = pos+np.array([0,0,0])
							
	return pos_current 


initial_position= np.array([0,0,0])
position_history = initial_position
i= int(1);
while i<=int(100):
		print ("i=",i)
		y = move(initial_position)
		print ("y=",y)
		print ("position_history before np.vstack=",position_history)
		position_history = np.vstack([position_history,y])
		print ("position_history AFTER np.vstack=",position_history)
		
		if abs(y[0]) == 10 or abs(y[1]) == 10 or abs(y[2]) == 10: 
			#print ("y=",y)
			break
		i += 1
		initial_position = y
		
#print (position_history,i)
#print (np.array(position_history[len(position_history)-1,:]))
#print (len(position_history)-1)
#dataset=np.array([position_history[:,0],position_history[:,1],position_history[:,2]])

z=position_history
#print (dataset)
fig=plt.figure()
axes=plt.axes(projection="3d")
axes.set_xlabel("x")
axes.set_ylabel("y")
axes.set_zlabel("z")
line=axes.plot3D(z[:,0],z[:,1],z[:,2],'red')
plt.show()


print ("z=",z)

