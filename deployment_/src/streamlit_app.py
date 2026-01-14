import streamlit as st
import eda
from transformer import DropColumnsTransformer, CityToRegionTransformer, DegreeMappingTransformer
import prediction

st.set_page_config(
    page_title='Student Depression Detection',
    layout='wide',
    initial_sidebar_state='expanded'
)

page = st.sidebar.selectbox('Pilih Halaman: ', ('EDA', 'Prediksi Level Depresi Kamu'))

if page == 'EDA':
    eda.run()
else:
    prediction.run()