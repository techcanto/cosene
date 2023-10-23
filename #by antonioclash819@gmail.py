#by antonioclash819@gmail.com
# GNU/GPL License
# Plotting cosine function

import math as m
import matplotlib.pylot as plt

def f(x):
    y = m.cos(x)
    return y

def g(x):
    y = m.sin(x)
    return y

# y = f(x)
# x = [0,2pi]

N = 10 # number of jumps
A = 0 #begin of range
B = 4*3.1416 #end of page

X = []
Y = []

X2 = []
Y2 = []


X.append(X)
dx = (B-A)/N
values = range(N+1)
x = A 
for jump in values:
    x = A + jump * dx # es mejor la multiplicaion
    y = f(x) 
    X.append(x)
    Y.append(y)
    #x = A + dx (no usar esto por el error)
    y = g(x)
    X2.append


    print(x,y)
plt.plot(X,y)
plt.scarter(X,Y,color="red")
#plt.scartter (X,Y, color="green")
plt.show()