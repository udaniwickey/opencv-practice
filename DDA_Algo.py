def ROUND(a):
	return int(a + 0.5)

def drawDDA(x1,y1,x2,y2):
	x,y = x1,y1
	xx, yy = [], []
	length = abs((x2-x1) if abs(x2-x1) > abs(y2-y1) else (y2-y1))
	dx = (x2-x1)/float(length)
	dy = (y2-y1)/float(length)
	print(ROUND(x),ROUND(y))
	xx.append(ROUND(x)); yy.append(ROUND(y))
	for i in range(length):
		x += dx
		y += dy
		print(ROUND(x),ROUND(y))
		xx.append(ROUND(x)); yy.append(ROUND(y))
	return xx, yy

xx, yy = drawDDA(2,5,10,20)


import matplotlib.pyplot as plt
import numpy as np

def plot_line(x1,y1,x2,y2):
	xx, yy = drawDDA(x1,y1,x2,y2)
	plt.scatter(xx, yy, label= "points", color= "red", marker= "x", s=30)
	plt.axis([0, max(xx)+1, 0, max(yy)+1])
	plt.grid()
	plt.show()


plot_line(2,5,10,20)
plot_line(3,2,4,7)