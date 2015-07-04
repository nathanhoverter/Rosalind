import matplotlib.pyplot as plt
import numpy as np

x = []
y = []

readfile = open('sampledata.csv', 'r')
sepfile = readfile.read().split('\n')
#creates array of strings
readfile.close()

for pair in sepfile:
	x_y = pair.split(',')
	x.append(float(x_y[0]))
	y.append(float(x_y[1]))

print x 
print y


plt.plot(x, y)

plt.title('matplotlib example title')

plt.xlabel('matplot x label')

plt.ylabel('matplot y label')

plt.show()