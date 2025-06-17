import streamlit as st
from transformers import pipeline
import time

# Hugging Face의 사전학습 모델을 불러와서 감정 분석(sentiment analysis)을 수행하는 데모
# load_model_no_cache(): 매번 새로 로딩 (캐시 사용 안 함)
# load_model_with_cache(): 처음 한 번만 로딩하고 이후 캐시 사용 (@st.cache_resource)


# 캐시 없이 모델 로딩 (매번 로딩)
def load_model_no_cache():
    st.write("❌ [non-cached] 모델을 로딩합니다...")
    start = time.time()
    model = pipeline("sentiment-analysis")
    st.write(f"⏱️ 로딩 시간: {time.time() - start:.2f}초")
    return model


# 캐시를 사용하는 모델 로딩 (한 번만 로딩됨)


def load_model_with_cache():
    st.write("✅ [cached] 모델을 로딩합니다... (처음 한 번만 실행됨)")
    start = time.time()
    model = pipeline("sentiment-analysis")
    st.write(f"⏱️ 로딩 시간: {time.time() - start:.2f}초")
    return model


# UI 구성
st.title("🤖 Streamlit Model Load Cache Test")

use_cache = st.radio("캐시를 사용할까요?", ["사용함", "사용 안 함"], index=0)

if st.button("🔁 모델 불러오기"):
    if use_cache == "사용함":
        model = load_model_with_cache()
    else:
        model = load_model_no_cache()

    # 입력 텍스트
    query = st.text_input("문장을 입력하세요", value="I love Streamlit!")
    if query:
        result = model(query)[0]
        st.write("🎯 분석 결과:", result)
