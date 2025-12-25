import requests
import plotly.express as px
# crea una chiamata all'API

url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"


headers = {"Accept": "application/vnd.github.v3+json"}

r = requests.get(url, headers=headers)

#converte l'oggetto response in dizionario
response_dict = r.json()

#esplora le info sui repository
repo_dicts = response_dict['items']
repo_names, stars = [], []

# Esamina il primo repository
for repo_dict in repo_dicts:
    repo_names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

# crea la visualizzazione
title = "Most-Starred Python Projects on GitHub"
labels = { "x": "Repository", "y": "Stars"}
fig = px.bar(x=repo_names, y=stars, title=title, labels=labels)
fig.update_layout(title_font_size=28, xaxis_title_font_size=20, yaxis_title_font_size=20)
fig.show()