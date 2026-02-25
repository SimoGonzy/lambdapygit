import streamlit as st
import sqlite3
from pathlib import Path

def listato(query, arg):
    cur = get_cur_db()
    query += " LIMIT ? OFFSET ?"
    cur.execute(query, arg)
    data = cur.fetchall()

    for row in data:
        with st.container(border=True):
            st.subheader(f"{row['title']}")
            st.write(f"ID: {row['id']} {f"lang: {row['locale']}" if 'locale' in row.keys() else ""}")
            
    

def get_cur_db():
    db_path = Path(__file__).with_name("netflixdb.sqlite")
    con = sqlite3.connect(db_path, isolation_level=None)
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    return cur