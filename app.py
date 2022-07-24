import streamlit as st
max_width: int = 1200,
max_width_100_percent: bool = False,
padding_top: int = 1,
padding_right: int = 1,
padding_left: int = 1,
padding_bottom: int = 1,
):
if max_width_100_percent:
    	max_width_str = f"max-width: 100%;"
else:
        max_width_str = f"max-width: {max_width}px;"
        
styl = f"""
    <style>
        .reportview-container .main .block-container{{
            {max_width_str}
            padding-top: {padding_top}rem;
            padding-right: {padding_right}rem;
            padding-left: {padding_left}rem;
            padding-bottom: {padding_bottom}rem;
        }}
        }}
    </style>
    """

st.header('''
App for Substracting 2 Numbers
''')

#Get input

st.subheader('Number input:')
first_num = st.number_input('FIRST NUMBER')
second_num = st.number_input('SECOND NUMBER')
  

result = first_num-second_num

st.subheader('Result')
st.markdown(styl, unsafe_allow_html=True,result)
