import streamlit as st

st.title("🧪 위젯 동작 실습 통합 예제")

# -----------------------------
# Step 1️⃣ 버튼 누르면 텍스트 출력
# -----------------------------
st.header("1️⃣ 버튼 누르면 텍스트 출력")

if "clicked" not in st.session_state:
    st.session_state.clicked = False

if st.button("클릭하세요!"):
    st.session_state.clicked = True

if st.session_state.clicked:
    st.success("🎉 버튼이 눌렸습니다!")

st.divider()  # 시각적 구분

# -----------------------------
# Step 2️⃣ selectbox 선택값 유지 (key 사용)
# -----------------------------
st.header("2️⃣ 선택값 기억하기 (selectbox + key)")

fruit = st.selectbox("좋아하는 과일을 선택하세요:", ["사과", "바나나", "포도"],
                     key="selected_fruit")

st.info(f"🍎 선택한 과일: {st.session_state.selected_fruit}")

st.divider()

# -----------------------------
# Step 3️⃣ 텍스트 입력 → 다른 페이지에서 접근 가능하게 저장
# -----------------------------
st.title("Step 3️⃣ - 입력값을 다른 페이지로 전달하기")

with st.form("name_form"):
    name = st.text_input("이름을 입력하세요:", key="user_name_form")
    submitted = st.form_submit_button("저장하고 다음 페이지로 이동")

if submitted:
    # session_state에 명시적으로 저장
    st.session_state["user_name"] = st.session_state["user_name_form"]
    st.success(f"{st.session_state.user_name}님, 저장되었습니다.")
    st.write("📄 좌측 사이드바에서 [1_입력값_확인] 페이지로 이동해보세요.")

    
# -----------------------------
# Step 4️⃣ key 실험 - 중복된 위젯 비교
# -----------------------------
st.header("4️⃣ key 실험 - 동일한 위젯을 두 번 쓰면 어떻게 될까?")

st.write("👇 아래 코드는 두 개의 `text_input()`을 key 없이 사용합니다.")

try:
    name1 = st.text_input("이름")
    name2 = st.text_input("이름")  # key 없이 동일한 label이면 확실히 에러 발생
except Exception as e:
    st.error(f"❌ 오류 발생: {e}")

st.write(f"✅ 입력된 이름 A: {name1}")
st.write(f"✅ 입력된 이름 B: {name2}")

# st.write("아래는 key를 지정해서 충돌을 피한 버전입니다:")

# name3 = st.text_input("이름 입력란 A", key="name_input_a")
# name4 = st.text_input("이름 입력란 B", key="name_input_b")

# st.write(f"✅ 입력된 이름 A: {name3}")
# st.write(f"✅ 입력된 이름 B: {name4}")
