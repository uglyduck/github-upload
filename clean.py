#random walk 
#How many steps a worm needs to take to reach a boundary that is n=10 steps away in each 6 directions?
# Can he go back? Yes. He can move UP, DOWN, LEFT, RIGHT, FORWARD, and BACKWARD.

# What is the average number of steps if a i=1000 of the bugs try to accomplish the same thing?


import numpy as np
import matplotlib.pyplot as plt
import random
# from pylab import *

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
	# else: pos_current = pos+np.array([0,0,0])
							
	return pos_current 

	
l=[]
steps=[]
distances=[]

for k in list(range(1,1000)):
		
	l.append(k)
	initial_position= np.array([0,0,0])
	position_history = initial_position
	i= int(1);
	while i<=int(500):
			y = move(initial_position)
			position_history = np.vstack([position_history,y])
			if abs(y[0]) == 10 or abs(y[1]) == 10 or abs(y[2]) == 10: 
				#print ("y=",y)
				break
			i += 1
			initial_position = y
			
	z=position_history

	# # Uncomment the following lines if you want to plot.
	# fig=plt.figure()
	# axes=plt.axes(projection="3d")
	# axes.set_xlabel("x")
	# axes.set_ylabel("y")
	# axes.set_zlabel("z")
	# line=axes.plot3D(z[:,0],z[:,1],z[:,2],'red')
	# plt.show()
	
	last_position=z[len(z)-1]
	distance=(last_position[0]**2+last_position[1]**2+last_position[2]**2)**0.5
	distance=round(distance,3)
	steps.append(len(z))
	distances.append(distance)
	
	print ("last position=",last_position)
	print ("steps =",len(z))
	print ("distance =",round(distance,3))
	
	# steps=steps.append(len(z))
	print ("steps=",steps)
	print ("distances=",distances)
	print ("l=",l)
	
	




x = steps
y = distances

# fig, ax = plt.subplots(nrows=2, ncols=1)

# plt.plot(l,x)
# plt.plot(l,y)

# plt.show()


fig = plt.figure()

plt.subplot(2, 1, 1)
plt.plot(l,x)

plt.subplot(2, 1, 2)
plt.plot(l,y)


plt.show()
