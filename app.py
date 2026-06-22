# app.py

import streamlit as st
from rag_qa import answer_question

st.title("Historical RAG Assistant")

query = st.text_input("Ask a question")

if st.button("Search"):

    result = answer_question(query)

    st.subheader("Answer")

    st.write(result)