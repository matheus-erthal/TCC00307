def f(x):
    return x*x+2

def F(y,x):
    return 2*x

x = []
y = []
yc = []

a = 0
b = 4
n = 20

h = (b-a)/n
alfa = 2

yc.append(alfa)

for i in range(n+1):
    x.append(i * (b - a) / n)
    y.append(f(x[i]))

for i in range(n):
    yc.append(yc[i] + h * F(yc[i], x[i]))

import matplotlib.pyplot as plt

plt.plot(x, y)
plt.plot(x, yc)
plt.show()