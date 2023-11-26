import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb

from app_home import home_app
from app_data import data_app

def main():
    st.title('인천시 주정차 허용구간 안내')

    menu = ['홈','데이터 확인','지역별 주정차 확인']

    choice = st.sidebar.selectbox('메뉴 선택',menu)

    if choice == menu[0] :
        home_app()
    elif choice == menu[1] :
        data_app()
    elif choice == menu[2] :
        pass



if __name__ == '__main__' :
    main()
