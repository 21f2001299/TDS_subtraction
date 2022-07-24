import streamlit as st
import  pandas as pd

st.write('''
#App for Substracting 2 Numbers
''')

#Get input

st.header('Number input:')

def user_input_features():
  first_num = st.number_input('FIRST_NUMBER')
  second_num = st.number_input('SECOND_NUMBER')
  
  data = {'FIRST_NUMBER':first_num,
          'SECOND_NUMBER':second_num
         }
  features = pd.DataFrame(data, index=[0])
  return features

df = user_input_features()
result = df.iloc[0,0]-df.iloc[0,1]

st.subheader('Result')
st.write(result)
