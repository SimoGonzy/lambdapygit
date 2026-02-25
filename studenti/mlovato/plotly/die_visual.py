import plotly.express as px
from die import Die

# crea un D6
die = Die()

# lancia il dado e salva i risultati su una lista
results=[]

for roll_num in range(1000):
    result = die.roll()
    results.append(result)
    # analizza i risultati
frequencies = []
# crea una lista da 1 a 6 per un D6
poss_results = range(1, die.num_sides+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

title = "Risultati di 1000 lanci di un D6"
labels = {"x": "Risultato", "y": "Frequenza dei lanci"}

# visualizza i risultati
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
fig.show()