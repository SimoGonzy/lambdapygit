from utils import listato
import streamlit as st

'''
per runnare

stremlit run main.py
'''

if "batch_id" not in st.session_state:
    st.session_state.batch_id = 0

def increment_batch():
    st.session_state.batch_id += 1
def decrement_batch():
    st.session_state.batch_id -= 1

col1, col2, col3 = st.columns([5,1,1])
with col1:
    st.subheader(f"Visualizzazione Set #{st.session_state.batch_id}")
with col2:
    st.button("Prev", use_container_width=True, on_click=decrement_batch)
with col3:
    st.button("Next", type="primary", use_container_width=True, on_click=increment_batch)

listato("select * from movie union select * from season order by title desc", (10, st.session_state.batch_id*10))