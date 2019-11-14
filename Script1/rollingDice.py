#! python3
# a program to roll dice
from random import randint
from plotly.graph_objs import Bar,Layout
from plotly import offline

class Dice():
    """A class to roll dice """
    def __init__(self,dice_num=6):
        self.dice_num=dice_num
    """Rolling the dice"""
    def roll(self):
        return randint(1,self.dice_num)
if __name__=='main':
    dice=Dice()
    #Make some roll and store the results in a list
    results=[]
    for i in range(100000):
        results.append(dice.roll())

    #Analyst the result
    frequencies=[]
    for i in range(1,dice.dice_num+1):
        frequencies.append(results.count(i))

    #Visualize the data with histogram
    x_values=list(range(1,dice.dice_num+1))
    bar_data=[Bar(x=x_values,y=frequencies)]

    x_axis_config={'title':'Results'}
    y_axis_config={'title':'Frequencie of results'}
    layout=Layout(title='Results of rolling dice 1000 times',xaxis=x_axis_config,yaxis=y_axis_config)
    offline.plot({'data':bar_data,'layout':layout},filename='d6.html')