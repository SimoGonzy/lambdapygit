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
repo_links, stars, hover_texts = [], [], []

# Esamina il primo repository
for repo_dict in repo_dicts:
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)
    stars.append(repo_dict['stargazers_count'])
    # costruisco i testi sul mouse hover
    owner = repo_dict['owner']['login'] # nome login dell'owner
    description = repo_dict['description']
    hover_text = f"{owner}<br />{description}"
    hover_texts.append(hover_text)

# crea la visualizzazione
title = "Most-Starred Python Projects on GitHub"
labels = { "x": "Repository", "y": "Stars"}
fig = px.bar(x=repo_links, y=stars, title=title, labels=labels, hover_name=hover_texts)
fig.update_layout(title_font_size=28, xaxis_title_font_size=20, yaxis_title_font_size=20)
fig.update_traces(marker_color="SteelBlue", marker_opacity=0.6)
fig.show()