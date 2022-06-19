import pandas as pd 
import matplotlib.pyplot as plt 
import math

x1 = 5
y1 = 3

x2 = -4
y2 = 1

values1 = [x1,x2]
values2 = [y1,y2]

data = pd.DataFrame({'N0': values1,'N1': values2})

def calculation():
    p0 = math.sqrt(((x2-x1)**2) + (y2-y1)**2)
    d = p0
    return d

A = [x1,y1]
B = [x2,y2]
result = pd.DataFrame({'Distance': [calculation()],'A': [A],'B': [B]})
result = result.rename(index={0: 'Values'})

plt.style.use('ggplot')
plt.plot(data['N0'],data['N1'],color='blue')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
result
