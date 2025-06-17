import streamlit as st
import pandas as pd
import time


@st.cache_data
def load_user_data():
    return pd.DataFrame({
        "이름": ["Alice", "Bob", "Charlie"],
        "직업": ["개발자", "디자이너", "데이터 분석가"]
    })


if "user_data" not in st.session_state:
    st.session_state["user_data"] = []


st.title("사용자 등록 & 목록 확인")

with st.form("add_user_form"):
    name = st.text_input("이름을 입력하세요:")
    job = st.text_input("직업을 입력하세요:")
    submitted = st.form_submit_button("추가하기")

    if submitted:
        if not name or not job:
            st.warning("이름과 직업을 모두 입력해야 합니다.")
        else:
            # 사용자 정보 추가
            st.session_state["user_data"].append({"이름": name, "직업": job})
            st.success(f"{name} 님이 추가되었습니다.")


st.subheader("전체 사용자 목록")

# 기본 데이터 + 새로 추가된 사용자 결합
df_base = load_user_data()
df_new = pd.DataFrame(st.session_state["user_data"])
df_total = pd.concat([df_base, df_new], ignore_index=True)

st.dataframe(df_total)

if st.button("❌ 사용자 추가 초기화"):
    st.session_state["user_data"] = []
    st.rerun()  # ← 여기 수정됨!
