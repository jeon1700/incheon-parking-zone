import streamlit as st




def home_app():
    st.text('인천광역시 도로별 주청자 허용구간 안내 사이트 입니다.')
    st.subheader('각 지역구의 주정차 공간을 안내합니다.')
    st.markdown('**[강화군],[옹진군],[연수구]**')
    st.text('해당 지역은 데이터 부족으로 제외됩니다.')

    img_url = 'https://cdn.daily.hankooki.com/news/photo/202004/20200401_1_bodyimg_650465.jpg'


    st.image(img_url)
