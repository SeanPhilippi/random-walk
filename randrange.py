from random import randrange, seed
from matplotlib import pyplot

seed(1)
series = [randrange(10) for i in range(10)]
pyplot.plot(series)
print('series', series)
print('series 2', series)

