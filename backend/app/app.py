import pandas as pd
import streamlit as st
import requests

st.set_page_config(layout="wide")

st.title("🏦 Banking Intelligence (F-OS)")

bank = st.selectbox("Select Bank", ["HDFC", "ICICI"])
question = st.text_input("Ask a banking question",
                         "Is this bank vulnerable to high rates?")

if st.button("Analyze"):
    with st.spinner("Analyzing..."):
        r = requests.get(
            "http://127.0.0.1:8000/ask",
            params={"bank": bank, "question": question}
        )
        data = r.json()

    st.subheader("LLM Analysis")
    st.write(data["answer"])


st.subheader("Key Metrics Trend")

df = pd.DataFrame({
    "Quarter": ["Q1", "Q2", "Q3"],
    "NIM": [3.9, 4.1, 4.2],
    "GNPA": [1.3, 1.2, 1.4]
})

st.line_chart(df.set_index("Quarter"))
