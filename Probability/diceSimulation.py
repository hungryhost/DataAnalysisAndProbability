import numpy as np
x = np.random.randint(1, 7, size=(2, 1000000))

y = x[0]  # кубик 1
z = x[1]  # кубик 2
count_same = 0  # количество бросков с равными числами
count_six = 0  # кол-во бросков с хотя бы 1-й 6-й
same1, same2 = [], []  # последовательность бросков с хотя бы одной 6-й
count_same_six = 0  # количество двойных шестерок в same

print("\nЭксперимент 1")
for i in range(100000):
	if y[i] == z[i]:
		count_same += 1
	if y[i] == 6 or z[i] == 6:
		count_six += 1
		same1.append(y[i])  # явно создаем новую последовательность опытов
		same2.append(z[i])

for i in range(len(same2)):
	if same1[i] == 6 and same2[i] == 6:
		count_same_six += 1

print("Кол-во бросков с хотя бы 1-й 6-ой:", count_six)
print("Кол-во бросков с одинаковыми числами:", count_same)
print("Кол-во бросков с двумя 6-ми:", count_same_six)
print("Доля двойных 6-к в новой последовательности:", count_same_six/count_six)

print("\nЭксперимент 2")

probability = 0.5
newSet1, newSet2 = 80000*[-1], 80000*[-1]  # массивы для последовательностей
new_count = 0  # количество бросков с хотя бы 1й 6й и вероятностью 0.5
n1, n2 = 0, 0  # переменные для цикла
for i in range(100000):
	p = np.random.binomial(1, probability)
	if p == 0:
		if y[i] == 6:
			newSet1[n1] = 6
			n1 += 1
		else:
			n1 += 1
	if p == 1:
		if z[i] == 6:
			newSet2[n2] = 6
			n2 += 1
		else:
			n2 += 1

for i in range(len(newSet2)):
	if newSet2[i] == 6 or newSet1[i] == 6:
		new_count += 1

print("Количество бросков с хотя бы 1-й 6-й (вторым алгоритмом):", new_count)
print("Доля двойных 6-к в новой последовательности:", count_same_six/new_count)
