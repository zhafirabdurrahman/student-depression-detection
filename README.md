
**File Description:**
- **README.md**  
  General project documentation  
- **modeling.ipynb**  
  Notebook containing Exploratory Data Analysis (EDA) and model development using the SVC algorithm  
- **inference.ipynb**  
  Notebook for model inference and testing using new data  
- **deployment**  
  Folder containing files used for model deployment with Streamlit and Hugging Face  
- **url.txt**  
  File containing URLs related to this project  

---

## 📖 Problem Background
Depression is one of the most common mental health disorders among students. It not only affects mental well-being but also has a significant impact on daily activities, particularly academic performance. Depression can lead to burnout, declining academic results, and even the decision to discontinue studies (dropout).

Therefore, depression must be addressed early to reduce potential long-term risks. One effective approach is early detection (_screening_) to identify whether a student is at risk of depression.

---

## 🎯 Project Output
The output of this project is a machine learning model capable of predicting student depression status (**Depressed** or **Not Depressed**) using the Support Vector Classifier (SVC) algorithm.  
The model is deployed using **Streamlit** and **Hugging Face**, allowing users to perform predictions by inputting new data.

---

## 📊 Data Description
- **Source:** Kaggle  
- **Dataset:** Student Depression Dataset  
- **Rows:** 27,901  
- **Columns:** 18  
- **Coverage:** Students from various cities in India  
- **Data Quality:** No missing values and no duplicate records  

Dataset link:  
https://www.kaggle.com/datasets/adilshamim8/student-depression-dataset

---

## 🔍 Methodology
This project uses **supervised machine learning** to classify student depression status (**Depressed** vs **Not Depressed**).  
The algorithm applied is **Support Vector Machine (SVM)** with a Support Vector Classifier (SVC).

---

## 🛠️ Tech Stack

| Category              | Tools / Libraries              |
|-----------------------|--------------------------------|
| Programming Language  | Python                         |
| IDE / Tools           | VS Code                        |
| Machine Learning      | scikit-learn                   |
| Data Manipulation     | pandas, numpy                  |
| Data Visualization    | matplotlib, seaborn            |
| Deployment            | Streamlit, Hugging Face        |

---

## 🔗 References
- [Academic Pressure and Adolescent Mental Health](https://labcito.co.id/tekanan-akademis/)
- [Model Deployment (Hugging Face)](https://huggingface.co/spaces/zhafirabd/student-depression-detection)
- [Dataset Source](https://www.kaggle.com/datasets/adilshamim8/student-depression-dataset)
