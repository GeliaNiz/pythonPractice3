import csv
from pprint import pprint
import urllib as ur
import pandas as pd
import requests as req
import matplotlib.pyplot as plt
url = 'https://raw.githubusercontent.com/Newbilius/Old-Games_DOS_Game_Gauntlet/master/GAMES.csv'
file = pd.read_csv(url,delimiter=';',names=['title', 'genre','url','year'])
pd.set_option('display.max_rows', None)

# Сброс ограничений на число столбцов
pd.set_option('display.max_columns', None)

# Сброс ограничений на количество символов в записи
pd.set_option('display.max_colwidth', None)

fig1, axs1 = plt.subplots(1, 1, figsize=(40, 25))
fig2, axs2 = plt.subplots(1,1, figsize=(40,25))
dict1 = {}
for i in file['year']:
    if i != 'не издана':
        dict1[i] = 0
for i in file['year']:
    if i != 'не издана':
        dict1[i] += 1
graph1 = axs1.bar(dict1.keys(), dict1.values())
axs1.set_title('the most popular year')
axs1.set_xlabel('years')
axs1.set_ylabel('released games, quantity')

dict80 = {}
dict90 ={}
dict2000 = {}
for i in file['genre']:
    dict80[i] = 0
for i in file.iterrows():
    if i[1].year != 'не издана':
        if int(i[1].year) <= 1990:
            dict80[i[1].genre] += 1

for i in file['genre']:
    dict90[i] = 0
for i in file.iterrows():
    if i[1].year != 'не издана':
        if 1990 < int(i[1].year) <= 2000:
            dict90[i[1].genre] += 1

for i in file['genre']:
    dict2000[i] = 0
for i in file.iterrows():
    if i[1].year != 'не издана':
        if int(i[1].year) > 2000:
            dict2000[i[1].genre] += 1
x1 =[]
y1 = []
for i in dict80:
    x1.append(i)
    y1.append(dict80.get(i))
x2 =[]
y2 = []

for i in dict90:
    x2.append(i)
    y2.append(dict90.get(i))

x3 =[]
y3 = []
for i in dict2000:
    x3.append(i)
    y3.append(dict2000.get(i))
axs2.set_title('genres popularity in 80th, 90th, 2000th')
axs2.set_xlabel('genres')
axs2.set_ylabel('games, quantity')
axs2.grid()
axs2.plot(x1, y1,'r',label='80th')
axs2.plot(x2, y2, 'g',label='90th')
axs2.plot(x3, y3,'b',label='2000th')
axs2.legend()
print(file)
plt.show()
