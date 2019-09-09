import matplotlib.pyplot as plot
import numpy as np
weightList=[35,47,90,56,78,61,49,69,53]
plot.hist(weightList,density=0.5, bins=20)

#plot.axis([20, 100, 0, 0.06]) 
#axis([xmin,xmax,ymin,ymax])
plot.xlabel('Weight')
plot.ylabel('Probability')
plot.show()
