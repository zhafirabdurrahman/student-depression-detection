import pickle
import pandas as pd
from transformer import CityToRegionTransformer, DropColumnsTransformer, DegreeMappingTransformer
import streamlit as st


def run():
    # Load the best svm model
    with open('./src/model_svm.pkl', 'rb') as model_file:
        loaded_model = pickle.load(model_file)
    # Pembuatan Form
    with st.form(key='student-depression-detection'):
        id = st.number_input('ID', min_value=0,max_value=28000, value= 0, help='ID Anda')
        age = st.slider('Age', min_value=18,max_value=55, value= 20, help='Usia Anda')
        academic = st.number_input('Academic Pressure', min_value=0,max_value=5, value= 3, help='Tekanan Akademik yang anda rasakan', step=1)
        work_pressure = st.number_input('Work Pressure', min_value=0,max_value=5, value= 3, help='Isi 0 jika anda masih pelajar', step=1)
        cgpa = st.number_input('CGPA', min_value=0.0,max_value=10.0, value= 7.0, help='Nilai Rata-rata GPA Anda Saat ini', step=0.1)
        study_satisfaction = st.number_input('Study Satisfaction', min_value=0,max_value=5, value= 3, help='Tingkat Kepuasan Anda saat menjalani studi', step=1)
        job_satisfaction = st.number_input('Job Satisfaction', min_value=0,max_value=5, value= 3, help='Isi 0 jika anda masih pelajar', step=1)
        study_hours = st.number_input('Work/Study Hours', min_value=0,max_value=12, value= 8, help='Lama anda melakukan kegiatan belajar', step=1)
        financial_stress = st.number_input('Financial Stress', min_value=1,max_value=5, value= 3, help='Kondisi Ekonomi saat ini', step=1)
        st.markdown('---')

        gender = st.selectbox('Gender', {'Male', 'Female'}, index= 0, help='Gender')
        city = st.selectbox('City', {'Visakhapatnam','Bangalore','Srinagar','Varanasi','Jaipur','Pune','Thane',
            'Chennai','Nagpur','Nashik','Vadodara','Kalyan','Rajkot','Ahmedabad',
            'Kolkata','Mumbai','Lucknow','Indore','Surat','Ludhiana','Bhopal',
            'Meerut','Agra','Ghaziabad','Hyderabad','Vasai-Virar','Kanpur','Patna',
            'Faridabad','Delhi','Unknown'}, index= 0, help='Tempat Tinggal Anda')
        profession = st.selectbox('Profession', {'Student','Civil Engineer','Architect','UX/UI Designer',
            'Digital Marketer','Content Writer','Educational Consultant','Teacher',
            'Manager','Chef','Doctor','Lawyer','Entrepreneur','Pharmacist'}, index= 11, help='Pekerjaan Anda saat ini')
        sleep_duration = st.selectbox('Sleep Duration', {'5-6 hours','Less than 5 hours','7-8 hours','More than 8 hours','Others'}, index= 0)
        dietary = st.selectbox('Dietary Habits', {'Healthy','Moderate','Unhealthy','Others'}, index= 1, help='Rata-rata jam tidur anda')
        degree = st.selectbox('Degree', {'B.Pharm','BSc','BA','BCA','M.Tech','PhD','Class 12','B.Ed','LLB','BE',
            'M.Ed','MSc','BHM','M.Pharm','MCA','MA','B.Com','MD','MBA','MBBS','M.Com',
            'B.Arch','LLM','B.Tech','BBA','ME','MHM','Others'}, index= 8, help='Sedang berada pada jenjang studi apa?')
        family = st.selectbox('Family History of Mental Illness', {'No', 'Yes'}, index= 0, help='Apakah ada keluarga yang mengalami mental illness?')
        suicidal_thought = st.selectbox('Suicidal Thoughts', {'No', 'Yes'}, index= 0, help='Suicidal Thought')

        submitted = st.form_submit_button('Predict')

    # Membuat DataFrame untuk dua user baru
    data_inf = {
        'id': id,
        'Gender': gender,
        'Age': age,
        'City': city,
        'Profession': profession,
        'Academic Pressure': academic,
        'Work Pressure': work_pressure,
        'CGPA': cgpa,
        'Study Satisfaction': study_satisfaction,
        'Job Satisfaction': job_satisfaction,
        'Sleep Duration': sleep_duration,
        'Dietary Habits': dietary,
        'Degree': degree,
        'Suicidal Thoughts': suicidal_thought,
        'Work/Study Hours': study_hours,
        'Financial Stress': financial_stress,
        'Family History of Mental Illness': family
    }

    data_inf = pd.DataFrame([data_inf])
    st.dataframe(data_inf)

    if submitted:
        prediction = loaded_model.predict(data_inf)[0]
        st.success(f"Hasil Prediksi: {prediction}")

if __name__ == '__main__':
    run()