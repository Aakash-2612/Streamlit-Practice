import streamlit as st


def BMI_calculator():
    st.title("BMI Calculator")

    with st.form('BMI Calculator'):
        col1, col2, col3 = st.columns([3, 2.5, 1])    # spaces for the columns

    with col1:
        weight = st.number_input('Enter your weight in Kg')

    with col2:
        height = st.number_input('Enter your height in cm')

    with col3:
        submit = st.form_submit_button('Calculate')

    if submit:
        BMI = round(weight / ((height/100)**2), 2)
        if BMI <= 18.5:
            st.error('Underweight')
        elif 18.5 < BMI <= 24.9:
            st.success('Healthy / Normal')
        elif 25 <= BMI <= 29.9:
            st.warning('Overweight')
        else:
            st.error('Obese')
