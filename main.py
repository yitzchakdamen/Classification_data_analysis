import streamlit as st
from src.SystemManagement import SystemManagement 

st.set_page_config(page_title="מערכת ניתוח טקסטים", layout="centered")
st.title("📊 מערכת ניתוח טקסטים – הפעלת עיבוד")

with st.form("activation_form"):
    
    st.header("הגדרות קלט")
    source_dir = st.text_input("📂 נתיב תיקיית מקור:", value="data")
    dest_dir = st.text_input("📁 נתיב תיקיית יעד:", value="results")
    upload_file_name = st.text_input("📄 שם קובץ המקור:", value="tweets_dataset")
    cleaningd_file_name = st.text_input("🧹 שם קובץ לאחר ניקוי:", value="cleaningd_tweets_dataset")
    analysis_results_file_name = st.text_input("📈 שם קובץ תוצאות הניתוח:", value="analysis_cleaningd")
    relevant_columns_raw = st.text_input("🔠 שמות עמודות רלוונטיות (מופרדות בפסיק):", value="Text,Biased")

    submitted = st.form_submit_button("🚀 הפעל עיבוד")

if submitted:
    try:
        relevant_columns = [col.strip() for col in relevant_columns_raw.split(",")]

        st.info("🔧 מריץ את מחלקת SystemManagement...")

        system_management = SystemManagement(source_file_directory=source_dir,destination_file_directory=dest_dir)

        system_management.activation(
            upload_file_name=upload_file_name,
            cleaningd_file_name=cleaningd_file_name,
            analysis_results_file_name=analysis_results_file_name,
            relevant_columns=relevant_columns
        )

        st.success("✅ העיבוד הסתיים בהצלחה!")
        
        df = system_management.file_handling.upload_results_json(analysis_results_file_name)

        st.subheader("📋 תצוגת תוצאה מתוך הקובץ שנשמר:")
        st.dataframe(df)

    except Exception as e:
        st.error(f"שגיאה במהלך ההרצה: {e}")
