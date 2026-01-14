# Judul Project
Student Depressin Detection

## Repository Outline
1. README.md - Penjelasan gambaran umum project
2. P1M2_muhammad_zhafir_abdurrahman.ipynb - Notebook yang berisi pengolahan data berupa EDA dan modeling menggunakan algoritman SVC.
3. P1M2_muhammad_zhafir_abdurrahman_inf - Notebook ini berisi pengujian model menggunakan data baru.
4. P1M2_muhammad_zhafir_abdurrahman_conceptual.txt - Berisi text mengenai jawaban dari pertanyaan conceptual.
5. deployment_ - folder yang berisi file yang digunakan dalam deployment model menggunakan streamlit dan hugging face.
6. url.txt - berisi url yang digunakan dalam project ini.

## Problem Background
Depresi merupakan salah satu gangguan kesehatan mental yang semakin sering terjadi dikalangan pelajar. Depresi tidak hanya menyebabkan masalah pada kesehatan mental tapi juga dapat berpengaruh pada kegiatan sehari-hari, hal yang terdekat pada pelajar adalah penurunan performa akademik, burnout, bahkan tidak ingin melanjutkan studi-nya (_drop out_). Sehingga depresi ini harus ditangani dengan baik untuk menghindari risiko risiko yang kemungkinan akan terjadi dimasa depan, salah satunya adalah dengan mendeteksi awal (_screening_) mengenai apakah pelajar berpotensi mengalami depresi atau tidak.

## Project Output
Output pada project ini adalah model yang dapat memprediksi tingkat depresi pada pelajar menggunkan algoritma SVC, hasil program dilakukan deployment menggunakan streamlit dan hugging face sehingga user dapat menggunakan program tersebut dengan menambahkan data baru

## Data
Sumber data berdasarkan dari dataset yang diambil dari situs [kaggle](https://www.kaggle.com/datasets/adilshamim8/student-depression-dataset), dataset berisi 18 Kolom dan 27901 baris, tiap baris berisi data pelajar yang tersebar pada berbagai kota di India, pada dataset ini tidak ada missing value dan data duplicate.

## Method
Project ini bertujuan untuk memprediksi tingkat depresi (Depressed, Not Depressed) menggunakan supervised machine learning, metode yang dipakai adalah model Support Vector Machine.

## Stacks
Adapun bahasa pemrograman, tools dan library yang digunakan pada project ini adalah:
1. python
2. VSCode
3. Streamlit
4. HuggingFace
5. scikit-learn
6. pandas
7. numpy
8. matplotlib
9. seaborn

## Reference
- [Artikel Tekanan Akademis Terhadap Mental Remaja](https://labcito.co.id/tekanan-akademis/)
- [Model Deployment](https://huggingface.co/spaces/zhafirabd/student-depression-detection)
- [Dataset](https://www.kaggle.com/datasets/adilshamim8/student-depression-dataset)