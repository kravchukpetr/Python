import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sts


x0 = 3
k = 4
pareto = sts.pareto(k, loc=0, scale=x0)
pareto_mean = pareto.mean()
pareto_std = pareto.std()
print 'Theoretical mean: %.2f'%pareto.mean()
print 'Theoretical standard dev: %.2f'%pareto.std()
print 2**0.5
# x = np.linspace(2.0,20.0,1000)
# r = pareto.rvs(size=1000)
# pdf = pareto.pdf(x)
# cdf = pareto.cdf(x)
# plt.plot(x, pdf)
# plt.plot(x, cdf)
# plt.hist(r, normed=True, histtype='stepfilled', alpha=0.2)
# plt.legend(loc='best', frameon=False)
# plt.show()

# x = np.linspace(2.0,20.0,1000)
# cdf = pareto.cdf(x)
# plt.plot(x, cdf, label = 'theoretical CDF')
# pdf = pareto.pdf(x)
# plt.plot(x, pdf, label = 'theoretical PDF')
# plt.ylabel('$number of samples$')
# plt.xlabel('$x$')
# plt.legend()
# plt.title("CDF (binomial)")
# plt.show()

n = 20
x = np.arange(1, 1000, 1)
mean_array = []
for i in x:
    mean_array.append(pareto.rvs(size=n).mean())
means_mean = np.mean(mean_array)
print means_mean
mu = means_mean
sigma = pareto_std/n**0.5
norm_rv = sts.norm(loc=mu, scale=sigma)
x = np.linspace(2.0,10.0,1000)
pdf = norm_rv.pdf(x)
plt.plot(x, pdf)
plt.hist(mean_array, normed=True, histtype='stepfilled', alpha=0.2)
plt.show()

# fisher
# dfn, dfd = 29, 19
# x = np.linspace(0.1,5.0,1000)
# rv = sts.f(dfn, dfd)
# r = sts.f.rvs(dfn, dfd, size=1000)
# mean, var, skew, kurt = sts.f.stats(dfn, dfd, moments='mvsk')
# print mean
#
# pdf = rv.pdf(x)
# # print rv.cdf(3)
# plt.plot(x, pdf)
# plt.hist(r, normed=True, histtype='stepfilled', alpha=0.2)
# plt.legend(loc='best', frameon=False)
# plt.show()
