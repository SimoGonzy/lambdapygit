from utils import listato, get_cur_db
import streamlit as st

from datetime import datetime


col1, col2 = st.columns([1,16],gap="xxsmall", vertical_alignment="bottom")
with col1:
    checkbox_title = st.checkbox("title", label_visibility="collapsed")
with col2:
    title = st.text_input("Titolo", placeholder="Es. Il più bel film del mondo!")
col1,col2 = st.columns([1,16],gap="xxsmall", vertical_alignment="bottom")
with col1:
    checkbox_year = st.checkbox("year", label_visibility="collapsed")
with col2:
    year = st.number_input("Anno di uscita", min_value=1970, max_value=2026, value=2020, step=1)
col1,col2 = st.columns([1,16],gap="xxsmall", vertical_alignment="bottom")
with col1:
    checkbox_language = st.checkbox("locate", label_visibility="collapsed")


cur = get_cur_db()
cur.execute("select distinct locale from movie")
list_dict_lingue = cur.fetchall()
lista_lingue = []
for language in list_dict_lingue:
    lista_lingue.append(language['locale'])
with col2:
    language = st.selectbox("Scegli la lingua", lista_lingue)
col1, col2, col3 = st.columns([10,1,10], vertical_alignment="center")
with col1:
    st.markdown("<p style='text-align: right;'>Movie</p>", unsafe_allow_html=True)
with col2:
    movie_season_toggle = st.toggle("")
with col3:
    st.markdown("<p style='text-align: left; margin-left: 10px'>Season</p>", unsafe_allow_html=True)

if "batch_id" not in st.session_state:
    st.session_state.batch_id = 0
if "query" not in st.session_state:
    st.session_state.query = "select * from movie"
if "params" not in st.session_state:
    st.session_state.params = (10, st.session_state.batch_id*10)
def show():
    condizioni = []
    parametri = []
    if checkbox_title and title:
        #titolo ok
        condizioni.append("title like ?")
        parametri.append(title)
    if checkbox_year:
        # anno Ok
        condizioni.append("release_date >= ? AND release_date < ?")
        parametri.append(datetime(year,1,1).timestamp()*1000)
        parametri.append(datetime(year+1,1,1).timestamp()*1000)
        
    if checkbox_language and language and not movie_season_toggle:
        # lingua ok
        condizioni.append("locale = ?")
        parametri.append(language)
    if not movie_season_toggle:
        st.session_state.query = "select * from movie"
    else:
        st.session_state.query = "select * from season"
    st.session_state.params = (10, st.session_state.batch_id*10)
    st.session_state.batch_id = 0
    if condizioni:
        st.session_state.query += " WHERE " + " AND ".join(condizioni)
        st.session_state.params = tuple(parametri+[10, st.session_state.batch_id*10])
    if orderby_selectbox == "Title":
        st.session_state.query += " order by title desc"
    else:
        st.session_state.query += " order by release_date asc"

def increment_batch():
    st.session_state.batch_id += 1
    list_temp = list(st.session_state.params)[:-1]
    list_temp.append(st.session_state.batch_id*10)
    st.session_state.params = list_temp
def decrement_batch():
    st.session_state.batch_id -= 1
    list_temp = list(st.session_state.params)[:-1]
    list_temp.append(st.session_state.batch_id*10)
    st.session_state.params = list_temp

col1, col2, col3, col4 = st.columns([2,5,2,2], vertical_alignment="bottom")
with col1:
    orderby_selectbox = st.selectbox("Order by", ['Title', 'Year'])
with col2:
    st.button("Calcola", type="primary", use_container_width=True, on_click=show)
with col3:
    st.button("Prev", use_container_width=True, on_click=decrement_batch)
with col4:
    st.button("Next", use_container_width=True, on_click=increment_batch)


listato(st.session_state.query, st.session_state.params)




