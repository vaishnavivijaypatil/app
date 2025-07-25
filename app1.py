import streamlit as st
import pandas as pd

# Create a form
with st.form("my_form"):
    name = st.text_input("Name")
    email = st.text_input("Email")
    submit_button = st.form_submit_button("Submit")

# Store data in CSV file
if submit_button:
    data = {"Name": [name], "Email": [email]}
    df = pd.DataFrame(data)
    try:
        existing_df=pd.read_excel("data.xlsx")
        combined_df=pd.concat([existing_df,df])
        combined_df.to_excel("data.xlsx",index=False)
    except FileNotFoundError:
        df.to_excel("data.xlsx",index=False)
    st.write("Successfully submitted")
    