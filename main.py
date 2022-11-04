import pyotp
import streamlit as st
import time
st.title('Python OTP Application')
st.subheader('Author : Jamy Laureys')
key = st.text_input("Key")
name = st.text_input("Name")
ph = st.empty()
N = 5
st.button("Reload")
totp = pyotp.TOTP(str(key))
st.header(name + " : " + totp.now())
