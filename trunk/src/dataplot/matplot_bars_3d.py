from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(12.5,6), dpi=100)
ax = fig.add_subplot(111, projection='3d')
for c, z in zip(['b', 'r', 'g'], [10, 5, 0]):
    xs = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
    ys = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])

    # You can provide either a single color or an array. To demonstrate this,
    # the first bar of each set will be colored cyan.
    cs = [c] * len(xs)
    cs[0] = 'c'
    ax.bar(xs, ys, zs=z, zdir='y', color=cs, alpha=0.8)

ax.set_xlabel('por Ano')
ax.set_ylabel('H / M / HM')
ax.set_zlabel('Numero de Inscritos')

plt.show()
