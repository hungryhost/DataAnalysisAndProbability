from scipy.stats import *
import matplotlib.pyplot as plt
import seaborn as sns
# settings for seaborn plotting style
sns.set(color_codes=True)
# settings for seaborn plot sizes
sns.set(rc={'figure.figsize':(5,5)})
data_binom = binom.rvs(n=10,p=0.3,size=100000) + \
             binom.rvs(n=30,p=0.8,size=100000)
data = []
x = binom.std(10,0.3,100000) + binom.std(30, 0.8, 100000)
y = binom.var(10,0.3,100000) + binom.var(30, 0.8, 100000)
m = binom.mean(10,0.3,100000) + binom.mean(30, 0.8, 100000)

for i in data_binom:
    if i <= 30:
        data.append(i)
ax = sns.distplot(data,
                  kde=False,
                  color='skyblue',
                  hist_kws={"linewidth": 1,'alpha':1})
ax.set(xlabel='Binomial Distribution', ylabel='Frequency')
print("---------- Binominal Distribution -------------")
plt.show()
print("STD:", x)
print("VAR:", y)
print("MEAN:", m)
data_expon = expon.rvs(scale=2,loc=0,size=100000) + \
             expon.rvs(scale=5,loc=0,size=100000)
ax = sns.distplot(data_expon,
                  kde=True,
                  bins=100,
                  color='skyblue',
                  hist_kws={"linewidth": 15,'alpha':1})
ax.set(xlabel='Exponential Distribution', ylabel='Frequency')
plt.show()
x = expon.std(0,2) + expon.std(0,5)
y =  expon.var(0,2) + expon.var(0,5)
m =  expon.mean(0,2) + expon.mean(0,5)
print("----------Exponential Distribution -------------")
print("STD:", x)
print("VAR:", y)
print("MEAN:", m)
data = []
data_poisson = poisson.rvs(mu=0.1, size=100000)
for i in range(99):
    data_poisson = data_poisson + poisson.rvs(mu=0.1, size=100000)
ax = sns.distplot(data_poisson,
                  bins=30,
                  kde=False,
                  color='skyblue',
                  hist_kws={"linewidth": 1,'alpha':1})
ax.set(xlabel='Poisson Distribution', ylabel='Frequency')
plt.show()
print("----------Poisson Distribution -------------")
print("STD:", data_poisson.std())
print("VAR:", data_poisson.var())
print("MEAN:", data_poisson.mean())