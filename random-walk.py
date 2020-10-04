# y(t) = y(t - 1) + e(random #)
# matplotlib
# plot a random walk in 1 dimension
# y starts at 0, x increases or decreases by 1, chosen randomly
# assign # of steps to take, and plot a visual line graph connecting all of the points

import matplotlib
from random import randint

coords = []
y = 0
steps = 200

# step 0 - 199
for step in range(steps):
    print('rand int', randint(-1, 1))
    y = y + randint(-1, 1)
    print('step, y', f'{step}, {y}')
    coords.append([step, y])
print('coords', coords)
