def fnc(x):
    y = np.sin(x/5.0)*np.exp(x/10.0) + 5.0*np.exp(-x/2.0)
    return y
def fnc1(x):
    y = 3.43914511 -0.18692825*x
    return y
def fnc2(x):
    y = 3.32512949 -0.06531159*x -0.00760104*x**2
    return y
def fnc3(x):
    y =  4.36264154-1.29552587*x + 0.19333685*x**2 -0.00823565*x**3
    return y
from matplotlib import pylab as plt
import numpy as np
from scipy import linalg

# plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
# plt.show()

i = [1.0, 4.0, 10.0, 15.0]
print(i)
x = np.array(i)
y = np.array(fnc(x))
z = np.array(y[:, np.newaxis])
print x
print y
print z
koef2 = np.array(x**2)
koef3 = np.array(x**3)
koef= np.array([[1.0, 1.0, 1.0, 1.0], [1.0, 4.0, 16.0, 64.0], [1.0, 10.0, 100.0, 1000.0], [1.0, 15.0, 225.0, 3375.0]])
print koef
#
w = linalg.solve(koef, z)
print w
# x =1
# y = np.sin(x/5.0)*np.exp(x/10.0) + 5.0*np.exp(-x/2.0)
# print(y)
# x =15
# y = np.sin(x/5.0)*np.exp(x/10.0) + 5.0*np.exp(-x/2.0)
# print(y)
# plt.plot(x, y)
# plt.show()
#
# a = np.array([[3, 2, 0], [1, -1, 0], [0, 5, 1]])
# b = np.array([1, 15])
#
# x = linalg.solve(a, b)

x = np.arange(1., 15., 0.01)
plt.plot(x, fnc(x), x, fnc3(x))
plt.show()

print fnc(4)
print fnc3(4)
string = str(round(w[0,0],2)) + ' ' + str(round(w[1,0],2))+ ' ' + str(round(w[2,0],2))+ ' ' + str(round(w[3,0],2))
# print(w[0,0])
# print(w[1,0])
# print(w[2,0])
# print(w[3,0])
string = str(w[0,0]) + ' ' + str(w[1,0])+ ' ' + str(w[2,0])+ ' ' + str(w[3,0])
print(string)
file_obj = open('submission-2.txt', 'w')
file_obj.write(string)
file_obj.close()
