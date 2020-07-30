import numpy as np
from matplotlib import pyplot as plt
#
X = np.random.randint(1, 7, size=(1, 100000))  # создаем массив бросков
y = X[0]
x = [i for i in range(100001)]
D = dict(zip(x, y))  # создаем соответствие времени и броска
indexes = []
diff = []
for i in D:
	if D[i] == 6:
		indexes.append(i)  # выбираем те броски, где выпала 6-ка
for i in range(len(indexes)-1):
	diff.append(indexes[i+1]-indexes[i])  # находим интервалы м/у 6-ми
K = []
for i in diff:
	if i <= 50:
		K.append(i)  # выбираем те интервалы, что меньше 50с
unique1, counts1 = np.unique(K, return_counts=True)
unique2, counts2 = np.unique(diff, return_counts=True)
newList = [x / len(diff) for x in counts1]
C1 = dict(zip(unique1, counts1))
C2 = dict(zip(unique2, counts2))
plt.bar(unique1, newList, align='center', width=0.5)
plt.show()


# задание 2

l = len(y)
a = []
b = []
c = 0
n = 0
for i in range(0, l+1, 50):
	a.append(y[i-50:i])  # разбиваем на группы по 50
a = a[1::]
N = []
n = 0
for i in a:
	c = 0
	for j in i:
		if j == 5 or j == 6:
			c += 1  # считаем 5-ки и 6-ки
	b.append(c)
	N.append(n)
	n += 1
B = []
for i in b:
	if i <= 50:
		B.append(i)
unique, counts = np.unique(B, return_counts=True)
newList = [x / len(a) for x in counts]
plt.bar(unique, newList, align='center', width=1)
plt.show()
print((counts))
print(np.asarray((unique, counts)).T)
