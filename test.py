import streamlit as st

st.title("Bé tập làm toán")
col1,col2,col3=st.columns(3)
with col1:
    a = st.number_input('a')
with col2:
    radio = st.radio('Phép toán', ('+', '-', 'x', ':'), horizontal=True)
with col3:
    b=st.number_input('b')
c=st.number_input('Nhập kết quả')
if st.button("Kiểm tra"):
    if radio=="+":
        result=a+b
    elif radio=="-":
        result=a-b
    elif radio=="x":
        result=a*b
    elif radio==":":
        result=round(a/b,2)
    
    if result==c:
        st.success("Chính xác")
        st.balloons()
    else:
        st.error(f'Sai, đáp số đúng là {result}')

