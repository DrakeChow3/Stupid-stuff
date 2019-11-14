#! python3
# a program rolling 2 dice(whatever side)

from plotly.graph_objs import Bar,Layout
from plotly import offline
from rollingDice import Dice
if __name__=='main':
    #Making two dices
    dice_1=Dice()
    dice_2=Dice()
    #Roll two dices 1000 times and counting the results
    results=[]
    for i in range(1000):
        results.append(dice_1.roll()+dice_2.roll())

    max_result=dice_1.dice_num+dice_2.dice_num
    frequecies=[]
    for i in range(2,max_result+1):
        frequecies.append(results.count(i))
    #Visualize the data
    x_data=list(range(2,max_result+1))
    bar_data=[Bar(x=x_data,y=frequecies)]

    x_axis_config={'title':'The X asix','dtick':1}
    y_axis_config={'title':'The y asix'}
    layout=Layout(title='Histogram of rolling 2 dice 1000 times',xaxis=x_axis_config,yaxis=
                y_axis_config)
    offline.plot({'data':bar_data,'layout':layout},filename='d6d10.html')