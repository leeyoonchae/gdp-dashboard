import streamlit as st
import pandas as pd
import time

# Step 1. 기본 상품 목록을 불러오는 함수 (캐시 사용)
@st.cache_data
def load_product_data():
    # 여기에 기본 상품 3개 정도를 반환하도록 작성하세요
    pass

# Step 2. 세션 상태 초기화
# 여기에 'product_list'라는 키가 없으면 빈 리스트로 초기화하도록 작성하세요

# Step 3. 상품 등록 폼
st.title("상품 등록 & 전체 상품 보기")

with st.form("add_product_form"):
    name = st.text_input("상품명 입력:")
    price = st.number_input("가격 입력:", min_value=0)
    submitted = st.form_submit_button("상품 등록")

    if submitted:
        # 가격이 0이면 경고 출력, 아니면 상품 정보 등록
        pass

# Step 4. 전체 상품 목록 출력
# load_product_data()로 기본 목록 불러오기
# session_state의 상품도 DataFrame으로 변환 후 병합하여 출력

# Step 5. 초기화 버튼 만들기 (session_state 초기화)
