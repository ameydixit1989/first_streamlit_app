
import streamlit

streamlit.title ('My parents new healthy Diner')
streamlit.title ('breakfast menu')
streamlit.title ('Omega 3 & blueberry Oatmeal')
streamlit.title ('Kale , spinach & rocket Smoothie')
streamlit.title ('Hard boiled free range egg')


import pandas 
my_fruit_list= pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
