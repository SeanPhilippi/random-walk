from random import random, seed
from matplotlib import pyplot

# random number generator with a start point of 1
# allows for consistent set of random numbers
seed(1)
# create a list
random_walk = list()
# if random number between 0 and 1 is less than .5, append -1,
# else append 1
random_walk.append(-1 if random() < .5 else 1)

for i in range(50):
    # randomly make movement -1 or 1
    movement = -1 if random() < .5 else 1
    # value to append to list for plot is the existing number +
    # a random 1 or -1
    value = random_walk[i] + movement
    # append the new value to the random_walk list
    random_walk.append(value)
# plot the list of coordinates
pyplot.plot(random_walk)
pyplot.show()
