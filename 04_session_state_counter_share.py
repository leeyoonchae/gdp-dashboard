import streamlit as st

# 매번 초기화하기 때문에 증가가 안 됨 0->1까지만 
st.title('Counter Example')
count = 0

increment = st.button('Increment')
if increment:
    count += 1

st.write('Count = ', count)

