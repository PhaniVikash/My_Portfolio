import pandas
import streamlit as st

# Front end code
st.set_page_config(layout="wide")
col1 , col2=st.columns(2)
with col1:
    st.image('images/Vikky.jpeg',width=350)
with col2:
    st.title("\t Kote Phani Vikash")
    content=("\n \t Hi This Vikash , This is the website to display all my projects. "
             "for any suggestions feel free to reach out to me.  phanivikash@gmail.com")
    st.info(content)

# Code to add all the app data
content2= 'Here are the list of programs that I have built ,  Thanks for visiting my page'
st.info(content2)
col3,empty_col,col4=st.columns([1.5,0.8,1.5])
df=pandas.read_csv('data.csv',sep=';')
with col3 :
    for index,row in df[:8].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image('images/' + row['image'])
        st.write(f"[Source Code]({row['url']})")

with col4 :
    for index,row in df[8:].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image('images/'+row['image'])
        st.write(f"[Source Code]({row['url']})")

