import streamlit as st
import pandas as pd

# 캐싱 미사용
#  Uber 승차 공유 데이터 세트 (50MB 크기의 CSV 파일)를 DataFrame으로 로드할 때 
# 캐싱을 사용하지 않으면 앱이 로드되거나 사용자 상호작용이 있을 때마다 다운로드가 다시 실행

def load_data(url):
    df = pd.read_csv(url)  # 👈 Download the data
    return df

df = load_data("https://github.com/plotly/datasets/raw/master/uber-rides-data1.csv")
st.dataframe(df)

st.button("Rerun")

