import streamlit as st

st.title("🎨 테마 적용 상태 확인")

st.markdown("**이건 진한 텍스트입니다.**")
st.text("일반 텍스트 색상은 textColor 기준입니다.")

st.checkbox("체크박스")  # ← primaryColor로 포인트가 적용됨
st.button("버튼")        # ← ❗ 기본 회색 버튼 (커스터마이징 거의 안 됨)

st.success("이건 성공 메시지 (색상 고정)")
st.info("이건 정보 메시지 (색상 고정)")
