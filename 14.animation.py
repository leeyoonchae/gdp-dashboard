import streamlit as st
import time

st.title("🎉 Streamlit 애니메이션 효과 모음")

# 버튼을 누르면 풍선
if st.button("축하해요! 🎈"):
    st.success("풍선 올라갑니다~!")
    st.balloons()

# 눈 내리는 효과
if st.button("겨울 느낌 내기 ❄️"):
    st.snow()

# 토스트 메시지
if st.button("토스트 메시지 🎉"):
    st.toast("작업이 완료되었습니다!", icon="🎉")

# 텍스트 점점 나타나기
if st.button("텍스트 천천히 보여주기"):
    messages = ["하나...", "둘...", "셋!", "끝났어요! 🎉"]
    for msg in messages:
        st.write(msg)
        time.sleep(1)
