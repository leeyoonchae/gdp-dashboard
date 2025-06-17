import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Welcome to Streamlit! 👋")

st.sidebar.success("Select a demo above.")

# 사용자 이름 입력
name = st.text_input("이름을 입력하세요", key="temp_user_name")

# 확인 버튼 눌러야만 user_name에 저장
if st.button("이름 확정"):
    st.session_state.user_name = name.strip()
    st.success("이름이 저장되었습니다!")


# ✅ 현재 상태 출력 (디버깅용)
st.markdown("#### 현재 session_state:")
st.json(st.session_state)

st.markdown(
    """
    ---
    Streamlit is an open-source app framework built specifically for
    Machine Learning and Data Science projects.

    **👈 Select a demo from the sidebar** to see some examples
    of what Streamlit can do!

    ### Want to learn more?
    - Check out [streamlit.io](https://streamlit.io)
    - Jump into our [documentation](https://docs.streamlit.io)
    - Ask a question in our [community forums](https://discuss.streamlit.io)

    ### See more complex demos
    - Use a neural net to [analyze the Udacity Self-driving Car Image Dataset](https://github.com/streamlit/demo-self-driving)
    - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
    """
)
