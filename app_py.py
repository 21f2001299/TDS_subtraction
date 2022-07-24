import streamlit as st

st.write('''
#App for Substracting 2 Numbers
''')

#Get input

st.header('Number input:')


first_num = st.number_input('FIRST_NUMBER')
second_num = st.number_input('SECOND_NUMBER')


st.write(f'The result of substracting {first_num} from {second_num} is: {first_num-SECOND_NUMBER}')
