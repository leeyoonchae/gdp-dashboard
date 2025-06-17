import streamlit as st

st.title("📦 tabs, popover, modal 예제")

# -----------------------------
# 1. Tabs (탭 인터페이스)
# -----------------------------
tab1, tab2, tab3 = st.tabs(["🐍 파이썬", "📊 데이터", "🎨 시각화"])

with tab1:
    st.subheader("🐍 파이썬 탭")
    st.code("print('Hello Streamlit!')", language="python")

with tab2:
    st.subheader("📊 데이터 탭")
    st.dataframe({"이름": ["홍길동", "김영희"], "점수": [95, 88]})

with tab3:
    st.subheader("🎨 시각화 탭")
    st.line_chart([10, 20, 15, 30])

st.divider()

# -----------------------------
# 2. Popover (설정 드롭다운 느낌)
# -----------------------------
with st.popover("⚙️ 설정 열기"):
    st.write("여기서 설정을 변경하세요.")
    theme = st.radio("테마 선택", ["라이트", "다크", "자동"])

    st.write(f"선택한 테마: {theme}")

st.divider()


# -----------------------------
# 3. Modal (모달 다이얼로그)
# -----------------------------
@st.dialog("📧 뉴스레터 신청하기")
def newsletter():
    name = st.text_input("이름")
    email = st.text_input("이메일")
    if st.button("제출"):
        st.session_state["newsletter"] = {"name": name, "email": email}
        st.rerun()


if "newsletter" not in st.session_state:
    if st.button("뉴스레터 모달 열기"):
        newsletter()
else:
    st.success(f"{st.session_state.newsletter['name']}님, 감사합니다!")
