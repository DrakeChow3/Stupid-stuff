#! python 3
# a program to visualize a random walk with matplotlib

from random import choice
import matplotlib.pyplot as plt

class RandomWalk:
    """ A class to generate random walk """
    def __init__(self,num_points=5000):
        """Initiate some of the variables"""
        self.num_points=num_points
        """Generate list of data starting from 0"""
        self.x_axis=[0]
        self.y_axis=[0]
        
    def fill_walk(self):
        """Calculate all the points in the walk"""
        
        """Keep the loop until we have 5000 walking points"""
        while len(self.x_axis) <= self.num_points:
            #Generate the x direction
            x_side=choice([1,-1])
            x_range= choice([0,1,2,3,4])
            x_step=x_side*x_range
            #Generate the y direction
            y_side=choice([1,-1])
            y_range= choice([0,1,2,3,4])
            y_step=y_range*y_side
            
            #If the walk standing still
            if x_step == 0 and y_step == 0:
                continue
            #Adding the direction to the list
            x_point=self.x_axis[-1]+x_step
            y_point=self.y_axis[-1]+y_step
            self.x_axis.append(x_point)
            self.y_axis.append(y_point)

rw=RandomWalk()
rw.fill_walk()         
plt.style.use('seaborn-talk')
fig,ax=plt.subplots()
num_p=range(rw.num_points+1)
ax.scatter(rw.x_axis,rw.y_axis,c=num_p,cmap=plt.cm.Blues,edgecolors='none',s=5)
plt.show()