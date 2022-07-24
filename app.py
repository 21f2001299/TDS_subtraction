import streamlit as st

st.header('''
App for Substracting 2 Numbers
''')

#Get input

st.subheader('Number input:')
first_num = st.number_input('FIRST NUMBER')
second_num = st.number_input('SECOND NUMBER')
  

result = first_num-second_num

st.subheader('Result')
st.markdown(result)
