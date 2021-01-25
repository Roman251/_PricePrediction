import streamlit as st
import pandas as pd
import plotly.express as px
from plot import chart_plot
from form import reg_form
from pred import pred_ins

regressor,X,y = pred_ins()
    
regressor.fit(X,y)


data = pd.read_csv("data//insurance.csv")
sample_data = data[0:15]
nav = st.sidebar.radio("Navigation",["Home","Prediction","Analytics","Form"])

if nav == "Home":
    st.title("Insurance")
    st.image("data/insurance.jpg", width=650)
    if st.checkbox("show sample_data"):
        st.dataframe(sample_data,width=800,height= 500)
    
    graph = st.checkbox("view_interactive_chart")
    if graph:
        val = st.slider("Filter data using years",0,70)
        data = data.loc[data["age"]>= val]
        fig = px.scatter(data, x="age", y="charges", color="smoker",
                title="insurance cost with respect to age")
        st.plotly_chart(fig)

if nav == "Prediction":
    st.title("Insurance Cost")
    st.header("how much would your insurance plan cost you?")

    age = st.number_input("enter your age",15,65,step = 1)
    bmi = st.number_input("enter your body-mass-index(bmi)",15.00,80.00,step=0.25)
    smoker = st.number_input("are you a smoker?",0,1,step = 1)
    
    pred = regressor.predict([[age,bmi,smoker]])[0]
    
    if st.button("Predict"):
        if round(pred)<0:
            st.error("there is no insurance scheme for this combination of variables!! please contact the company")
        else:
            st.success(f"Your predicted insurance cost is {round(pred)}")

if nav == "Analytics":
    st.header("charts showing the insurance predictors")
    chart_plot()


if nav == "Form":
    st.header("Registration Form")
    reg_form()






