import email.utils as email
import json
import math
import urllib.request as request
import time
from pprint import pprint
import matplotlib.pyplot as plt

pr3url = 'https://raw.githubusercontent.com/true-grue/kispython/main/pract3/'
# get messages.json---------------
with request.urlopen(pr3url + 'messages.json') as url:
    data = json.loads(url.read().decode())
messages = {(m["subj"].upper(), time.strptime(m["date"].split(' (')[0], '%a, %d %b %Y %H:%M:%S %z')) for m in data}
# ------------------------------------
# get table.json----------------------
with request.urlopen(pr3url + 'table.json') as url:
    table = json.loads(url.read().decode())

# ---------------------------------------
# get failed.json------------------------
with request.urlopen(pr3url + 'failed.json') as url:
    fail = json.loads(url.read().decode())
pprint(fail)
# --------------------------------------
fig, axs = plt.subplots(2, 2, figsize=(20, 20))
fig3, axs3 = plt.subplots(1, 1, figsize=(40, 25))
fig4, axs4 = plt.subplots(1, 1, figsize=(40, 25))
fig6, axs6 = plt.subplots(1,1, figsize=(100,100))
# question1------------------------
axs[0][0].set_title('students daily activity')
dict1 = {}
for i in range(24):
    dict1[i] = 0

for i in messages:
    dict1[i[1][3]] += 1
graph1 = axs[0][0].plot(dict1.keys(), dict1.values())
axs[0][0].grid()
axs[0][0].set_xlabel("time, h")
axs[0][0].set_ylabel("messages, quantity")
# ---------------------------------
# question2------------------------
days_of_week = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}
axs[0][1].set_title('students weekly activity')
dict2 = {}
for i in range(7):
    dict2[days_of_week[i]] = 0
for i in messages:
    dict2[days_of_week[i[1][6]]] += 1
graph2 = axs[0][1].bar(dict2.keys(), dict2.values(), zorder=3)
axs[0][1].grid(zorder=0)
axs[0][1].set_xlabel("days of week")
axs[0][1].set_ylabel("messages, quantity")
# question3----------------------------
dict3 = {}
for i in messages:
    dict3[i[0].split(' ')[0]] = 0
for i in messages:
    dict3[i[0].split(' ')[0]] += 1
graph3 = axs3.bar(dict3.keys(), dict3.values())
axs3.set_title('groups activity')
axs3.set_xlabel('groups')
axs3.set_ylabel('messages,quantity')
# --------------------------------------
# question4------------------------------
for i in dict3.keys():
    dict3[i] = 0
for i in table['data']:
    if i[3] == 1:
        dict3[i[0]] += 1
graph4 = axs4.bar(dict3.keys(), dict3.values())
axs4.set_title('groups performance')
axs4.set_xlabel('groups')
axs4.set_ylabel('right solutions, quantity')
# ------------------------------------------
# question5------------------------------
dict5 = {}
for i in table['data']:
    dict5[i[2]] = 0
for i in table['data']:
    if i[3] == 0:
        dict5[i[2]] += 1
graph5 = axs[1][0].bar(dict5.keys(), dict5.values())
axs[1][0].set_title('the hardest task')
axs[1][0].set_xlabel('tasks')
axs[1][0].set_ylabel('false solutions, quantity')
# ---------------------------------------------
# question6--------------------------------------
dict6 = {'Incorrect test': 0,
         'referenced before assignment': 0,
         'is not defined': 0,
         'invalid literal ': 0,
         'list index out of range': 0,
         'побитовые операции': 0,
         'positional argument': 0,
         "module 'math' has no attribute 'ln'": 0,
         'pow expected 2 arguments': 0,
         'unsupported operand type': 0,
         'could not convert': 0,
         'None':0
         }

def contains_error(errors):
    for i in errors:
        for j in dict6.keys():
            if j in str(i):
                dict6[j] += 1
                print(j)
        else:
            dict6['Incorrect test'] += 1


for i in fail.values():
    contains_error(i)

graph6 = axs6.pie(dict6.values())
axs6.set_title('type errors')
axs6.legend(title='types', loc='center right', labels=dict6.keys(), prop={'size': 6})
# ------------------------------------------------
plt.show()
