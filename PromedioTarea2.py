import numpy as np
import pylab as pl
x = [1, 2, 3, 4]
pl.xlabel('Semestre')
y = [8.75, 8.83, 8.5, 8.7]
pl.ylabel('Promedio')
pl.plot (x,y, 'ro')
pl.plot (x,y)
pl.savefig('temp1.png')
pl.show()
