
import streamlit as st
from sample_data import sample_assessments
from utils import embed_assessments, search_assessments

st.title("SHL Assessment Recommender")

query = st.text_area("Enter Job Description or Query")
if st.button("Get Recommendations"):
    embeddings = embed_assessments(sample_assessments)
    results = search_assessments(query, sample_assessments, embeddings)
    for res in results:
        st.markdown(f"### [{res['name']}]({res['url']})")
        st.write(f"**Type**: {res['type']}")
        st.write(f"**Duration**: {res['duration']}")
        st.write(f"**Remote**: {res['remote_support']}, **Adaptive/IRT**: {res['adaptive_support']}")
        st.markdown("---")
