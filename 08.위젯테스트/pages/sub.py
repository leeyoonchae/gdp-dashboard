import streamlit as st

st.title("📄 다른 페이지에서 값 불러오기")

if "user_name" in st.session_state and st.session_state.user_name:
    st.success(f"✅ 저장된 이름: {st.session_state.user_name}")
else:
    st.warning("이름이 아직 입력되지 않았습니다. 메인 페이지에서 입력해주세요.")
