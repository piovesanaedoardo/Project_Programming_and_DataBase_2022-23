import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# streamlit run .\project.py

# ---- DataFrame & cleaning ---- 
mXmh_df = pd.read_csv('mxmh_survey_results.csv')
# Column 'Age': replacing the null values (only one) with the mean from the Age column
mXmh_df['Age'] = mXmh_df['Age'].fillna(mXmh_df['Age'].mean())
# Column 'Primary streaming service': replacing the null values (only one) with the string 'No one'
mXmh_df['Primary streaming service'] = mXmh_df['Primary streaming service'].fillna('No one')

mXmh_df.info()

st.header('Music & Mental Healt')
st.subheader('Survey results on music taste and self-reported mental health')

st.sidebar.subheader('Settings')

if st.sidebar.checkbox('Display DataFrame'):
    st.write('The DataFrame')
    st.write(mXmh_df)