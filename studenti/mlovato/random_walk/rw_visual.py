import matplotlib.pyplot as plt
from random_walk import RandomWalk


# crea un passeggiata aleatoria
rw = RandomWalk(50_000)
rw.fill_walk()

# plotta i punti della passeggiata
plt.style.use("classic")
fig, ax = plt.subplots(figsize=(10,6), dpi=128)
point_number = range(rw.num_points)
ax.scatter(rw.x_value, rw.y_value, c=point_number, cmap=plt.cm.Blues, edgecolors="none", s=1) # type: ignore
# stessa spaziatura delle tacche
ax.set_aspect("equal")
# il primo punto (0,0) è verde e più grande 
ax.scatter(0,0,c="green",edgecolors="none", s=100)
# l'ultimo punto è rosso e più grande
ax.scatter(rw.x_value[-1],rw.y_value[-1], c="red",edgecolors="none", s=100)
# eliminare gli assi
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)
plt.show()