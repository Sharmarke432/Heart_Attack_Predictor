import streamlit as st
import pandas as pd
import pickle

# Heart Attack Predictor App


#
df = pd.read_csv("HeartAttack.csv")

# Set the title and header of the app
st.title("Heart Attack Predictor App")
st.header("Predict the likelihood of a heart attack")

#Let user input their name
name = st.text_input("Enter your name:", "", key ="name_input")


#to find bounds for my features I will calculate interquartile range 
def upper_lower_bounds(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return lower_bound, upper_bound

if(name):
    st.write(f"Hello, {name}! Let's predict your heart attack risk.")

    #First feature will be age with limits being 0-120
    feature1 = st.number_input("Age:", min_value=0, max_value=120, value=0)
    
    #Second feature will be heart rate
    lower_bound, upper_bound = upper_lower_bounds(df, 'Heart rate')
    feature2 = st.number_input("Heart rate:", min_value=lower_bound, max_value=upper_bound, value=70.0)


