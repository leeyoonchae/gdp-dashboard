# 메인 진입 파일을 실행

#  Streamlit 1.33 이상에서 새로 도입된 기능인 st.Page()와 st.navigation()을 활용한 멀티 페이지 구성 방식입니다.
# 이전 방식(pages 폴더 + 여러 스크립트)보다 훨씬 간결하고 코드에서 직접 페이지 전환을 제어할 수 있다는 장점

import streamlit as st

# Define the pages
main_page = st.Page("mainPage.py", title="Main Page", icon="🎈")
page_2 = st.Page("page2.py", title="Page 2", icon="❄️")
page_3 = st.Page("page3.py", title="Page 3", icon="🎉")

# Set up navigation
pg = st.navigation([main_page, page_2, page_3])

# Run the selected page
pg.run()
