import pandas as pd
import matplotlib as mtl
import numpy as np
import matplotlib.pyplot as plt

fbd = pd.read_csv("filename_1.csv", delimiter=';', sep='\s*,\s*', encoding="windows-1251")

sbd = pd.read_csv("filename_2.csv", delimiter=';', sep='\s*,\s*', encoding="windows-1251")

tbd = pd.read_csv("filename_3.csv", delimiter=';', sep='\s*,\s*', encoding="windows-1251")

groupedDb = sbd.groupby(['Номер рейса', 'Город прилета']).size()


def by_cities(sdat):
    """
    this function determines from how often people fly from every city
    :return: int[from moscow; from st pet.]
    """
    borm = sdat.groupby(["Город вылета"]).size()

    cities = []
    for i in borm:
        cities.append(i)
    return cities

def rating_by_gender(fdat, sdat):
    """
    this function calculates ratings of each company
    :param fbd: 1st data base
    :param sbd: 2nd data base
    :return: 4 arrays as [[1st], [2nd], [3rd]]; followed as (bad, best, good, ok)
    """
    grades = []
    best = [[], [], []]
    good = [[], [], []]
    ok = [[], [], []]
    bad = [[], [], []]
    ident = []
    borm = fdat.groupby(["№паспорта", "Номер рейса"]).size().unstack()
    form = fdat.groupby(["Номер рейса", "Оценка"]).size().unstack()
    forms = fdat.groupby(["Номер рейса", "Оценка"]).size()
    #print(forms["KL402"])
    #print(forms["KL402"][0])
    for i in form:
        grades.append(i)
    for i in borm:
        ident.append(i)
    sumlb = 0
    sumub = 0
    sumwb = 0
    n = 0
    m = 0
    k = 0
    for i in ident:
        if i[1] == 'L':
            sumlb = sumlb + forms[i]["Плохо"]
            n+=1
        if i[1] == 'U':
            sumub = sumub + forms[i]["Плохо"]
            m+=1
        if i[1] == 'W':
            sumwb = sumwb + forms[i]["Плохо"]
            k+=1
    bad[0].append(sumlb)
    bad[1].append(sumub)
    bad[2].append(sumwb)
	return bad


def rating(firstbd, thirdbd):
	avia = pd.DataFrame(firstbd)
	dtbd = pd.DataFrame(thirdbd)
	rat = dtbd.groupby(
		['Серия']
		).agg(
		{
			'Средняя оценка полета': "mean"})
	rat.rename(columns={'Серия': 'Серия', 'Средняя оценка полета': 'Рейтинг'}, inplace=True)
	new = pd.merge(rat, avia, on=('Серия', 'Серия'))
	rati = pd.merge(dtbd,new, on =('Серия', 'Серия'))
	rati = rati[["Средняя оценка полета", "Авиакомпания"]]
	fig = plt.figure()
	ax = fig.add_subplot(1, 1, 1)
	fig.suptitle('')
	rati.boxplot(ax=ax, column='Средняя оценка полета', by=['Авиакомпания'], rot=45, fontsize=11, grid=True)
	title_boxplot = ''
	plt.title(title_boxplot)
	plt.suptitle('')
	plt.show()


def popularity(firstbd, thirdbd):
	avia = pd.DataFrame(firstbd)
	dtbd = pd.DataFrame(thirdbd)
	pop = dtbd.groupby(
		['Серия']
	).agg(
		{
			'Количество пассажиров': "sum"})
	pop.rename(columns={'Серия': 'Серия', 'Количество пассажирова': 'Сумма пассажиров'}, inplace=True)
	new_pop = pd.merge(pop, avia, on=('Серия', 'Серия'))
	new_pop = new_pop[["Авиакомпания", "Количество пассажиров"]]
	fig = plt.figure()
	ax = fig.add_subplot(1, 1, 1)
	new_pop.plot(x='Авиакомпания', ax=ax, kind='barh')
	plt.show()


def averageEconom(firstbd, thirdbd):
	avia = pd.DataFrame(firstbd)
	dtbd = pd.DataFrame(thirdbd)
	rat = dtbd.groupby(
		['Серия']
	).agg(
		{
			'Цена за эконом': "mean"})
	rat.rename(columns={'Серия': 'Серия', 'Цена за эконом': 'Средняя цена за эконом'}, inplace=True)
	new = pd.merge(rat, avia, on=('Серия', 'Серия'))
	new_pop = new[["Средняя цена за эконом", "Авиакомпания"]]
	fig = plt.figure()
	ax = fig.add_subplot(1, 1, 1)
	new_pop.plot(kind='bar', ax=ax, x='Авиакомпания', y="Средняя цена за эконом")
	plt.show()


def averageBusiness(firstbd, thirdbd):
	avia = pd.DataFrame(firstbd)
	dtbd = pd.DataFrame(thirdbd)
	rat = dtbd.groupby(
		['Серия']
	).agg(
		{
			'Цена за бизнес': "mean"})
	rat.rename(columns={'Серия': 'Серия', 'Цена за бизнес': 'Средняя цена за бизнес'}, inplace=True)
	new = pd.merge(rat, avia, on=('Серия', 'Серия'))
	new_pop = new[["Средняя цена за бизнес", "Авиакомпания"]]
	fig = plt.figure()
	ax = fig.add_subplot(1, 1, 1)
	fig.suptitle('')
	new_pop.plot(kind='bar', ax=ax, y='Средняя цена за бизнес', x='Авиакомпания')
	title_boxplot = ''
	plt.title(title_boxplot)
	plt.suptitle('')
	plt.show()


def month_popularity(thirdbd):
	general = pd.DataFrame(thirdbd)
	rat = general.groupby(
		['Месяц']
	).agg(
		{
			'Количество пассажиров': "sum"})
	print(rat)
	rat.rename(columns={'Месяц': 'Месяц', 'Количество пассажиров': 'Сумма пассажиров'}, inplace=True)
	fig = plt.figure()
	ax = fig.add_subplot(1, 1, 1)
	fig.suptitle('')
	rat[['Сумма пассажиров']].plot(kind='hist', ax=ax, bins=12)
	title_boxplot = ''
	plt.title(title_boxplot)
	plt.suptitle('')
	plt.show()


def monthMeanEconom(thirdbd):
	general = pd.DataFrame(thirdbd)
	rat = general.groupby(
		['Месяц']
	).agg(
		{
			'Цена за эконом': "mean"})
	rat.rename(columns={'Месяц': 'Месяц', 'Цена за эконом': 'Средняя цена эконом-класс'}, inplace=True)
	fig = plt.figure()
	ax = fig.add_subplot(1, 1, 1)
	fig.suptitle('')
	rat.plot(kind='bar', ax=ax, by='Месяц')
	title_boxplot = ''
	plt.title(title_boxplot)
	plt.suptitle('')
	plt.show()


def monthMeanBusiness(thirdbd):
	general = pd.DataFrame(thirdbd)
	rat = general.groupby(
		['Месяц']
	).agg(
		{
			'Цена за бизнес': "mean"})
	rat.rename(columns={'Месяц': 'Месяц', 'Цена за бизнес': 'Средняя цена бизнес-класс'}, inplace=True)
	fig = plt.figure()
	ax = fig.add_subplot(1, 1, 1)
	fig.suptitle('')
	rat.plot(kind='bar', ax=ax, by='Месяц')
	title_boxplot = ''
	plt.title(title_boxplot)
	plt.suptitle('')
	plt.show()


def numPopular(secbd, thirdbd):
	numb = pd.DataFrame(secbd)
	dtbd = pd.DataFrame(thirdbd)
	rat = dtbd.groupby(
		['Номер']
	).agg(
		{
			'Количество пассажиров': "sum"})
	rat.rename(columns={'Серия': 'Серия', 'Количество пассажиров': 'Популярность'}, inplace=True)
	new = pd.merge(rat, numb, on=('Номер', 'Номер'))
	new = new[["Популярность", "Номер"]]
	fig = plt.figure()
	ax = fig.add_subplot(1, 1, 1)
	new.plot(kind='scatter', ax=ax, x="Номер", y='Популярность')
	plt.show()
