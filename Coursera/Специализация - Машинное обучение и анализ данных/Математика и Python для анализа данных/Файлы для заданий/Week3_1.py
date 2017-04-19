def fnc(x):
    y = np.sin(x/5.0)*np.exp(x/10.0) + 5.0*np.exp(-x/2.0)
    return y
def h(x):
    y = fnc(x)
    return y.astype(int)
def f(x):   # The rosenbrock function
    return .5*(1 - x[0])**2 + (x[1] - x[0]**2)**2

from matplotlib import pylab as plt
import numpy as np
from scipy import optimize

x = np.arange(1., 50., 0.01)
# x0 = [1.3, 0.7, 0.8, 1.9, 1.2]
plt.plot(x, fnc(x))
# plt.show()
print int(fnc(2))
print optimize.minimize(fnc, 30, method='BFGS')
answer1 = round(optimize.minimize(fnc, 2, method='BFGS').fun,2)
answer2 = round(optimize.minimize(fnc, 30, method='BFGS').fun,2)
# print answer1
# print answer2
string = str(answer1) + ' ' + str(answer2)
print(string)
# file_obj = open('submission-3.txt', 'w')
# file_obj.write(string)
# file_obj.close()

result = optimize.differential_evolution(fnc, [(1, 30)])
print result
for keys, values in result.items():
    if keys == 'fun':
        answer3 = round(values,2)
string2 = str(answer3)
print(string2)
# file_obj = open('submission-4.txt', 'w')
# file_obj.write(string2)
# file_obj.close()

# f2= np.vectorize(h(x))
# plt.plot(x,f2(x))
plt.plot(x, fnc(x), x,h(x))
plt.show()
answer4 = round(optimize.minimize(h, 30, method='BFGS').fun,2)
result2 = optimize.differential_evolution(h, [(1, 30)])
print result2
for keys, values in result2.items():
    if keys == 'fun':
        answer5 = round(values,2)
string3 = str(answer4) + ' '  + str(answer5)
print(string3)
# file_obj = open('submission-5.txt', 'w')
# file_obj.write(string2)
# file_obj.close()