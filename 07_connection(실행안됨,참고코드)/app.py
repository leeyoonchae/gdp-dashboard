# 실행 안 되면 패키지 설치
# pip install streamlit gspread pandas

import streamlit as st

# Google Sheets 연결 객체 생성
conn = st.connection("gsheets", type="gspread")

# 시트에서 데이터 가져오기 (Sheet1 범위)
df = conn.read(spreadsheet="Sheet1", usecols=[0, 1, 2])  # 컬럼은 상황에 따라 조정

st.title("📄 Google Sheets 연결 예제")
st.write("시트에서 가져온 데이터:")
st.dataframe(df)
