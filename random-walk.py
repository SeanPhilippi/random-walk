import matplotlib
import matplotlib.pyplot as ppt
from random import randint

matplotlib.use('TkAgg')

coords = []
y = 0
x = 0
z = 0
steps = 200

# step 0 - 199
for step in range(steps):
    y = y + randint(-1, 1)
    x = x + randint(-1, 1)
    z = z + randint(-1, 1)
    coords.append([x, y, z])

xs = []
ys = []
zs = []

for [x, y, z] in coords:
    xs.append(x)    
    ys.append(y)    
    zs.append(z)    

ax = ppt.axes(projection='3d')
ax.set_title('3D Random Walk')

ppt.plot(xs, ys, zs, color='c', linestyle='--')
ppt.show()
ppt.savefig("mygraph.png")

