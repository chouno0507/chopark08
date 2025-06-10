import streamlit as st
import pandas as pd

# CSV 또는 Excel 파일 불러오기
@st.cache_data
def load_data():
    df = pd.read_excel("성별_임금_및_근로조건_규모_학력_연령계층별__20250610151838.xlsx", sheet_name="데이터", header=1)
    df[['성별(1)', '사업체규모별(1)', '학력별(1)', '연령별(1)']] = df[['성별(1)', '사업체규모별(1)', '학력별(1)', '연령별(1)']].ffill()
    return df

df = load_data()

st.title("📊 학력·기업규모별 근로조건 비교 분석")

# 선택 필터
selected_education = st.selectbox("학력을 선택하세요:", sorted(df["학력별(1)"].dropna().unique()))
selected_scale = st.selectbox("기업 규모를 선택하세요:", sorted(df["사업체규모별(1)"].dropna().unique()))

# 필터링
filtered = df[(df["학력별(1)"] == selected_education) & (df["사업체규모별(1)"] == selected_scale)]

# 표시할 주요 지표
columns_to_show = {
    "총근로시간 (시간)": "총 근로시간",
    "근로일수 (일)": "근로일수",
    "월임금총액 (천원)": "월 임금총액",
    "정액급여 (천원)": "정액급여"
}

st.subheader("📌 근로조건 지표")
for col, label in columns_to_show.items():
    if col in filtered.columns:
        avg_val = filtered[col].mean()
        st.metric(label=label, value=f"{avg_val:,.1f}")

# 표와 차트
st.subheader("📉 연령대별 비교 차트")
st.line_chart(filtered.set_index("연령별(1)")[list(columns_to_show.keys())])
