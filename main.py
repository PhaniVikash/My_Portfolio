import pandas
import streamlit as st

# Design web page ( Home )
st.set_page_config(layout="wide")
col1 , col2=st.columns(2)
with col1:
    st.image('images/phani_vikash.jpeg',width=350)
with col2:
    st.title("\t Kote Phani Vikash")

    # Code to add all the app data
    content = ("\n \t Hello, I'm Vikash. This website features all the projects I have worked on.\n"
               "For any suggestions feel free to reach out to me.  phanivikash@gmail.com")
    st.info(content)

    with open("phani_vikash_resume.pdf", "rb") as file:
        resume_data = file.read()

    # Add download button
    st.download_button(
        label="Download My Resume",
        data=resume_data,
        file_name="Phani_Vikash_Resume.pdf",
        mime="application/pdf"
    )

st.info("My Git hub Link : https://github.com/PhaniVikash?tab=repositories")

col3,empty_col,col4=st.columns([1.5,0.8,1.5])
df=pandas.read_csv('data.csv',sep=';')
with col3 :
    for index,row in df[:7].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image('images/' + row['image'])
        st.write(f"[Source Code]({row['url']})")

with col4 :
    for index,row in df[7:].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image('images/'+row['image'])
        st.write(f"[Source Code]({row['url']})")


st.info("My LinkedIN Profile Link : https://www.linkedin.com/in/phani-vikash-83554b224/")
