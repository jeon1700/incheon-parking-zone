import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



def data_app():
    st.subheader('종합 데이터 확인')
    df = pd.read_csv('./data/incheon.csv')
    

    if st.checkbox('통계데이터') :
        st.dataframe(df.describe())
    else :
        st.text('')



