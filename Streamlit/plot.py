import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sbn
import altair as alt

sbn.set_style('darkgrid')

data = pd.read_csv("data//insurance.csv")

def chart_plot():
    fig1, axs1 = plt.subplots(ncols = 3, figsize = (20,5))
    sbn.distplot(data['age'], ax = axs1[0])
    sbn.distplot(data['bmi'], ax = axs1[1])
    sbn.distplot(data['charges'], ax = axs1[2])
    st.pyplot(fig1)

    st.subheader("From the graphs, we can see that:")

    st.text("1. Only bmi variable has a normal shape.") 
    st.text("2. Charges appears to highly skewed.")
    st.text("3. Regarding age, there are more patients in their early-twenties than the rest of age ranges.")

    chart = alt.Chart(data).mark_circle().encode(
        x = 'bmi',y='charges',color='smoker',tooltip =['bmi','charges']
    )
    st.altair_chart(chart,use_container_width = True)
    #use_container_width =True --> uses the whole column width
    
    st.text("People who smoke pay more in insurance.") 

    base = alt.Chart(data).mark_circle().encode(
        x = 'bmi', y = 'charges', color = 'children', tooltip =['bmi','charges']
    )
    st.altair_chart(base,use_container_width = True)

    st.text("There seems to be no correlation between having children and insurance costs")

    bar_chart = alt.Chart(data).mark_bar().encode(
        x = 'sex',y='count()', color='smoker', tooltip =['sex', 'count()']
    )
    st.altair_chart(bar_chart,use_container_width = True)

    fig, (ax1,ax2) = plt.subplots(nrows=1, ncols=2,figsize=(12,5))


    # instead of plt, use ax
    # fig --> container holding the plots.  can have multiple plots
    # axis --> actual plots

    ax1.hist(data['age'], bins = range(15, 70, 5), edgecolor = 'white', color = 'lightblue')
    ax1.set_xlabel('Age')
    ax1.set_ylabel('Count')
    ax1.set_title('Insurance by AgeGroup')

    charges = data.groupby('region').charges.mean().values
    gender = data.groupby('region').charges.mean().index

    ax2.bar(gender,charges, edgecolor='black')
    ax2.set_xlabel("region")
    ax2.set_ylabel("charges")
    st.pyplot(fig)

### SCATTER PLOT WITH HUE USING MATPLOTLIB

# x = data['bmi']
# y = data['charges']
# smoker = data['smoker']
# colors = {"yes":"red","no":"blue"}
# ax3.scatter(x, y, c=smoker.apply(lambda x: colors[x]))



#run this file

#chart_plot()