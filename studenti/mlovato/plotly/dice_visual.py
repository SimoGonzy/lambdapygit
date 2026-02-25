import plotly.express as px
from die import Die

# crea due dadi
die_1 = Die()
die_2 = Die(10)

# lancia il dado e salva i risultati su una lista
results=[]

for roll_num in range(50_000):
    result = die_1.roll() + die_2.roll()
    results.append(result)
    # analizza i risultati
frequencies = []
# crea una lista di possibili risultati
max_results = die_1.num_sides + die_2.num_sides
poss_results = range(2, max_results+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

title = "Risultati di 50.000 lanci di un D6 e un D10"
labels = {"x": "Risultato", "y": "Frequenza dei lanci"}

# visualizza i risultati
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
# mette le etichette a tutte le barre, altrimenti di default ne salta alcune
fig.update_layout(xaxis_dtick=1)
fig.show() # fig.write_html("dice_visual_d6d10.html") # to save instead of showing