from random import randint
from time import sleep
import matplotlib.pyplot as plt

# Initialization
population = int(input())
height = int(input())
width = int(input())
field = [[0 for x in range(height)] for y in range(width)]
percent = float(input())
tolerant = float(input())
steps = int(input())
colors = ['red', 'green']


def freeCell():
    currX = randint(0, width - 1)
    currY = randint(0, height - 1)
    while field[currX][currY] != 0:
        currX = randint(0, width - 1)
        currY = randint(0, height - 1)
    return currX, currY


def initState():
    first = int(population * percent)
    second = population - first
    for i in range(first):
        currX, currY = freeCell()
        field[currX][currY] = 1
    for i in range(second):
        currX, currY = freeCell()
        field[currX][currY] = 2


def is_happy(x, y):
    all = 0
    same_c = 0
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            if i >= 0 and j >= 0 and i<width and j<height:
                if field[i][j] != 0:
                    all += 1
                if field[x][y] == field[i][j]:
                    all += 1
                    same_c += 1
    if same_c/all >= tolerant:
        return True
    else:
        return False

def updateField():
    cont_happy = 0
    for i in range(width):
        for j in range(height):
            if not is_happy(i,j):
                newX, newY = freeCell()
                field[newX][newY] = field[i][j]
                field[i][j] = 0
            else:
                cont_happy += 1
    return cont_happy

def distance():
    all = 0
    coord = 0
    for i in range(width):
        for j in range(height):
            if field[i][j] != 0:
                all += 1
                coord += i
                coord += j
    return coord/all



# DrawField
initState()
fig, axs = plt.subplots(1, 3, figsize=(15, 5))
axs[0].set_title('steps animation')
a = axs[0].imshow([[x for x in y] for y in field], plt.get_cmap('rainbow'))
x = []
y = []
y1 = []
graph1 = axs[1].plot(x, y1)
graph2 = axs[2].plot(x, y)
figure = plt.figure(1)
plt.show(block=False)
for i in range(steps):
    happy = updateField()
    a.set_data([[x for x in y] for y in field])
    x.append(i)
    y.append(happy)
    y1.append(distance())
    axs[1].set_title('agents average position')
    graph1 = axs[1].plot(x, y1, color='r')
    axs[2].set_title('agents mood')
    graph2 = axs[2].plot(x, y, color='g')
    figure.canvas.draw()
    figure.canvas.flush_events()
    sleep(0.09)