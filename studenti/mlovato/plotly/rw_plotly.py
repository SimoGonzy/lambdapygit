import plotly.express as px

from random_walk import RandomWalk

rw = RandomWalk(50_000)

fig = px.scatter(x=rw.x_values, y=rw.y_values, color=range(0,rw.num_passi), color_continuous_scale="Blues")
fig.show()