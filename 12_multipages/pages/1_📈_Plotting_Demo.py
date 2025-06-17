import streamlit as st
import time
import numpy as np

st.set_page_config(page_title="Plotting Demo", page_icon="📈")

st.markdown("# Plotting Demo")
st.sidebar.header("Plotting Demo")

# ✅ 사용자 이름 출력 (이전 페이지에서 입력된 이름 활용)
user_name = st.session_state.get("user_name", "").strip()
if user_name:
    st.write(f"👋 {user_name}님, 반갑습니다!")
else:
    st.warning("👋 이름이 아직 입력되지 않았습니다. 메인 페이지에서 이름을 입력해주세요.")

# ✅ 클릭 수 상태 초기화
if "click_count" not in st.session_state:
    st.session_state.click_count = 0

# ✅ 차트 데이터 상태 초기화
if "chart_data" not in st.session_state:
    st.session_state.chart_data = np.random.randn(1, 1)

# ✅ 버튼 클릭 시 클릭 수 증가
if st.button("눌러보세요 (클릭 수 증가)"):
    st.session_state.click_count += 1

st.write(f"🔢 지금까지 버튼을 누른 횟수: {st.session_state.click_count}")

st.write("""
This demo illustrates a combination of plotting and animation with Streamlit.  
We're generating a bunch of random numbers in a loop for around 5 seconds. Enjoy!
""")

# ✅ 차트 그리기
progress_bar = st.sidebar.progress(0)
status_text = st.sidebar.empty()
chart = st.line_chart(st.session_state.chart_data)
last_rows = st.session_state.chart_data

for i in range(1, 101):
    new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
    status_text.text(f"{i}% 완료")
    chart.add_rows(new_rows)
    progress_bar.progress(i)
    last_rows = new_rows
    time.sleep(0.01)

# ✅ 다음 실행을 위한 데이터 저장
st.session_state.chart_data = last_rows
progress_bar.empty()

# 재실행 버튼
st.button("Re-run")
