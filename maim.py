import streamlit as st


st.title('Hello World')
st.write('This is a simple Streamlit app.')


if st.button('Say hello'):
   st.text('Hello, Streamlit!')


name = st.text_input('Please enter your name:')
if name:
   st.write(f'Hello, {name}!')
age=st.text_input('please enter your age:')
if age:
   st.write(f'my,{age}!')


if st.file_uploader('Please upload a file:', type=['txt', 'csv']):
   st.write('Thanks for uploading a file!')

if st.button('click'):
   st.write('hello ,hiii')



