import streamlit as st
import pandas as pd

st.title("📊 학력·기업규모별 근로조건 비교 분석")
st.image("2503072.png")
# 파일 업로더
uploaded_file = st.file_uploader("📁 엑셀 파일을 업로드하세요", type=["xlsx"])

if uploaded_file:
    df = pd.read_excel(uploaded_file, sheet_name="데이터", header=1)
    df[['성별(1)', '사업체규모별(1)', '학력별(1)', '연령별(1)']] = df[['성별(1)', '사업체규모별(1)', '학력별(1)', '연령별(1)']].ffill()

    st.success("✅ 파일 업로드 및 처리 완료!")

    selected_education = st.selectbox("학력을 선택하세요:", sorted(df["학력별(1)"].dropna().unique()))
    selected_scale = st.selectbox("기업 규모를 선택하세요:", sorted(df["사업체규모별(1)"].dropna().unique()))

    filtered = df[(df["학력별(1)"] == selected_education) & (df["사업체규모별(1)"] == selected_scale)]

    st.subheader("📌 근로조건 지표")

    columns_to_show = {
        "총근로시간 (시간)": "총 근로시간",
        "근로일수 (일)": "근로일수",
        "월임금총액 (천원)": "월 임금총액",
        "정액급여 (천원)": "정액급여"
    }

    for col, label in columns_to_show.items():
        if col in filtered.columns:
            avg_val = filtered[col].mean()
            st.metric(label=label, value=f"{avg_val:,.1f}")

    st.subheader("📉 연령대별 비교 차트")
    st.line_chart(filtered.set_index("연령별(1)")[list(columns_to_show.keys())])
else:
    st.info("👆 왼쪽 위에서 엑셀 파일을 업로드하세요.")
