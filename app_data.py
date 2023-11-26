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

    st.text('최대 / 최소 데이터 확인하기')
    column_list = df.columns[ 4 : ]
    selected_columns = st.selectbox('컬럼을 선택하세요', column_list)

    st.text(selected_columns + ' 컬럼의 최소값')
    st.dataframe(df.loc[df[selected_columns] == df[selected_columns].min() , ])
    st.text(selected_columns + ' 컬럼의 최대값')
    st.dataframe(df.loc[df[selected_columns] == df[selected_columns].max() , ])

    st.text(selected_columns + ' 컬럼의 히스토그램')

    fig1 = plt.figure()
    df[selected_columns].hist(bins = 20)
    st.pyplot(fig1)    


