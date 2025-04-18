import streamlit as st
from send_email import send_email

st.header("Contact me")
with st.form(key='email'):
    email_id=st.text_input("Your E-mail")
    sub = st.text_input("Subject of email")
    raw_message=st.text_area("Enter your message ")

    message=f'''\
Subject : {sub}

from: {email_id}    
{raw_message}'''

    button=st.form_submit_button("Submit")

    if button:
        send_email(message)
        st.info("Your email sent successfully")
