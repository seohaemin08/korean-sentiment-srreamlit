import streamlit as st

# 기분에 따른 음식 추천 사전
mood_foods = {
    "행복해요 😊": ["아이스크림", "스시", "딸기 케이크"],
    "우울해요 😔": ["초콜릿", "라멘", "마라탕"],
    "화가 나요 😡": ["매운 떡볶이", "불닭볶음면", "버거"],
    "피곤해요 😩": ["삼계탕", "보양식", "비타민 주스"],
    "설레요 💓": ["마카롱", "샴페인", "파스타"],
    "지루해요 😐": ["치킨", "피자", "분식"]
}

# Streamlit 앱 구성
st.set_page_config(page_title="기분별 음식 추천기", page_icon="🍽️")

st.title("🍽️ 오늘의 기분에 어울리는 음식은?")
st.write("지금 기분을 선택하면, 어울리는 음식을 추천해드릴게요!")

# 기분 선택
mood = st.selectbox("당신의 현재 기분은 무엇인가요?", list(mood_foods.keys()))

# 추천 음식 표시
if mood:
    st.subheader(f"💡 '{mood}' 기분일 때 어울리는 음식:")
    for food in mood_foods[mood]:
        st.markdown(f"- {food}")
