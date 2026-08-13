import streamlit as st
from supabase.database.config import supabase
import time
from src.database.db import enroll_student_to_subject
@st.dialog('Enroll in Subject')
def enroll_dialog():
    st.write('Enter the Subject Code provided by your teacher to Enroll')
    join_code = st.text_input('Subject Code',placeholder='CS101')
    

    if st.button("Enroll now",type='primary',width = 'stretch'):
        if join_code:
            res = supabase.table('subjects').select('subject_id,name,subject_code').eq('subject_code',join_code).execute()
            if res.data:
                subject = res.data[0]
                student_id = st.session_state.subject['subject_id']

                check = supabase.table("subject_students").select('*').eq('subject_id',subject['subject_id']).eq('student_id',student_id).execute()
                 if check.data:
                    st.warning('You are already enrolled in this program')

                 else:
                    enroll_student_to_subject('subject_id',subject['subject_id'])
                    st.success('Successfully! Enrolled')
                    st.timesleep(1)
                    st.rerun()
    
        else:

           st.warning('Please enter the subject code')

