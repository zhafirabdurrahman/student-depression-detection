import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image
import numpy as np

def run():
    # Membuat title
    st.title('Program Prediksi Tingkat Depresi Pada Pelajar')

    # Membuat Sub Header
    st.subheader('Exploratory Data Analysis by Muhammad Zhafir Abdurrahman')

    # Menambah Gambar
    gambar = Image.open('./src/image.jpg')
    st.image(gambar, caption='Mental Health Matter')

    # Menambahkan Teks
    st.write('## Mengapa Tingkat Depresi Pada Pelajar Perlu di Analisis?')
    st.write('''Depresi merupakan salah satu gangguan kesehatan mental yang semakin sering terjadi dikalangan pelajar.
             Depresi tidak hanya menyebabkan masalah pada kesehatan mental tapi juga dapat berpengaruh pada kegiatan sehari-hari, hal yang terdekat pada pelajar adalah penurunan performa akademik, burnout, bahkan tidak ingin melanjutkan studi-nya (_drop out_).
             Sehingga depresi ini harus ditangani dengan baik untuk menghindari risiko risiko yang kemungkinan akan terjadi dimasa depan, salah satunya adalah dengan mendeteksi awal mengenai apakah pelajar berpotensi mengalami depresi atau tidak.
             ''')

    df = pd.read_csv("./src/student_depression_dataset.csv")
    st.dataframe(df)

    # Membuat Bar Plot
    st.write('### Bar Plot Perbandingan Tingkat Depresi Berdasarkan Gender')

    ct = df.groupby(['Gender', 'Depression']).size().unstack()

    labels = ct.index
    not_dep = ct[0]
    dep = ct[1]

    x = np.arange(len(labels))
    width = 0.35
    fig, ax = plt.subplots(figsize=(14, 8))

    ax.bar(x - width/2, not_dep, width, label='Not Depressed')
    ax.bar(x + width/2, dep, width, label='Depressed')

    ax.set_xlabel('Gender')
    ax.set_ylabel('Count')
    ax.set_title('Depression Levels by Gender')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    st.pyplot(fig)

    # Membuat Histogram berdasarkan User Input
    st.write('### Plot Histogram Berdasarkan User Input')
    fig = plt.figure(figsize=(16, 5))
    opsi = st.selectbox('Pilih Kolom : ', ('Age', 'CGPA', 'Work/Study Hours', 'Academic Pressure'))
    sns.histplot(df[opsi], bins=30, kde=True)
    st.pyplot(fig)

if __name__ == '__main__':
    run()