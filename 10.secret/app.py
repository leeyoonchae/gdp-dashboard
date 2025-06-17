import streamlit as st

# secrets.toml 값 읽기
api_key = st.secrets["api"]["key"]
base_url = st.secrets["api"]["base_url"]

st.title("🔐 API 키 테스트")
st.write(f"✅ API 키: `{api_key}`")  # 예시 출력용 (실제 앱에선 노출 금지!)
st.write(f"🌐 Base URL: {base_url}")
