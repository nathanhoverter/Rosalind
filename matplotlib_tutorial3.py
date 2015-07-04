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

#print x 
#print y

fig = plt.figure()
rect = fig.patch
rect.set_facecolor('white')

ax1 = fig.add_subplot(1, 1, 1, axisbg='white')
ax1.plot(x, y, 'c', linewidth=3.3)
ax1.set_title('title')
ax1.set_xlabel('quibit')
ax1.set_ylabel('qPCR')


plt.show()