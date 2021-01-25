import streamlit as st
import pandas as pd

def reg_form():
    
    first , last = st.beta_columns(2)
    first = first.text_input("first Name",value = "first name")
    last = last.text_input("last Name", value = "last name")
    
    email , phn = st.beta_columns([2,1]) # will divide the column in the ratio 2:1
    email = email.text_input("Email ID",value="mail")
    phn = phn.text_input("Mob number",value="phone")

    agr,but2,sub = st.beta_columns([2,4,2])
    # but2 will be used for blank space

    agree  = agr.checkbox("everything okay!!")
    submit = sub.button("submit")
    
    if submit:
        if agree:
            st.info("you will soon be contacted!! stay healthy")
            to_add = {"first_name":[first],"last_name":[last],"email_id":[email],"phone":[phn]}
            to_add = pd.DataFrame(to_add)
            to_add.to_csv("data//user_details.csv",mode='a',header = False,index= False)   # mode = a --> mode = appended 
        else:
            st.warning("Please Check the T&C box")

    