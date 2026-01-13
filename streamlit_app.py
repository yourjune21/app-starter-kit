import streamlit as st
import pandas as pd

# 페이지 설정
st.set_page_config(page_title="합격 여부 조회 시스템", page_icon="🎓")

st.title("🎓 합격 여부 조회")
st.write("이름과 생년월일을 입력하여 합격 여부를 확인하세요.")

# 데이터 불러오기
@st.cache_data
def load_data():
    return pd.read_csv("results.csv")

df = load_data()

# 사용자 입력창
with st.form("lookup_form"):
    name_input = st.text_input("이름", placeholder="예: 홍길동")
    birth_input = st.text_input("생년월일", placeholder="예: 1995-01-01")
    submit = st.form_submit_button("조회하기")

if submit:
    if name_input and birth_input:
        # 데이터 검색 (공백 제거 및 대조)
        result = df[(df['name'].str.strip() == name_input.strip()) & 
                    (df['birthday'].str.strip() == birth_input.strip())]
        
        if not result.empty:
            status = result.iloc[0]['status']
            if status == "합격":
                st.success(f"🎉 축하합니다! {name_input}님은 **합격**입니다.")
            else:
                st.error(f"😔 안타깝지만 {name_input}님은 **불합격**입니다.")
        else:
            st.warning("입력하신 정보와 일치하는 데이터가 없습니다. 다시 확인해 주세요.")
    else:
        st.info("이름과 생년월일을 모두 입력해 주세요.")
