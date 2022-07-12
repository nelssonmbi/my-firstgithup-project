import streamlit
streamlit.title("my Wife new health Dinner")
streamlit.header("Breakfast Manu")
streamlit.text('omega 3 $ blueberry Oatmeal')
streamlit.text('kale, Spinach $ rocket smothie')
streamlit.text('Hard-Boiled Free Range Egg')
import pandas as pd
my_fruit_list=pandas.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
streamlit.dataframe(my_fruit_list)
