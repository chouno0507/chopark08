import streamlit as st
import pandas as pd

# 제목
st.title("대학교별 취업률 상위 10")

# 엑셀 파일 경로
file_path = "대학교별_취업률_상위10_샘플.xlsx"

# 엑셀 파일 읽기
df = pd.read_excel(file_path)

# 데이터 미리보기
st.subheader("데이터 미리보기")
st.dataframe(df)

# 꺾은선 그래프 출력
st.subheader("취업률 상위 10 대학 꺾은선 그래프")
st.line_chart(df.set_index("대학명")["졸업 후 취업률 (%)"])
