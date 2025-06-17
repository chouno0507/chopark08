import streamlit as st
import pandas as pd

# 엑셀 파일 읽기
df = pd.read_excel("대학교별_졸업생_평균연봉_샘플.xlsx")

# 제목
st.title("대학교별 졸업생 평균연봉 및 취업률")

# 데이터 표시
st.subheader("데이터 미리보기")
st.dataframe(df)

# 꺾은선 그래프
st.subheader("졸업생 평균연봉 및 취업률 (꺾은선 그래프)")
st.line_chart(df.set_index("대학명")[["졸업생 평균연봉 (만원)", "취업률 (%)"]])
