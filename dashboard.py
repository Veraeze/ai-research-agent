import streamlit as st
import os
import pandas as pd

st.set_page_config(page_title="AI Research & Summary Dashboard", layout="wide")

st.title("AI Research & Summary Dashboard")
st.markdown("Search a topic, view scraped content, and see AI-generated summaries.")

# Get list of available topics from output folder
summary_files = [f for f in os.listdir("output") if f.endswith("_summary.txt")]
topics = [f.replace("_summary.txt", "") for f in summary_files]

topic_choice = st.selectbox("Select a topic to view:", topics)

if topic_choice:
    # path to the summary file
    raw_path = f"data/{topic_choice}.txt"
    summary_path = f"output/{topic_choice}_summary.txt"

    # load the raw content
    if os.path.exists(raw_path):
        with open(raw_path, "r", encoding="utf-8") as file:
            raw_content = file.read()
        st.subheader("Raw Scraped Content")
        st.text_area("Raw Content", raw_content, height=300)
    else:
        st.warning(f"No raw content found for topic: {topic_choice}, run web scraping first.")

    # load the summary 
    if os.path.exists(summary_path):
        with open(summary_path, "r", encoding="utf-8") as file:
            summary_text = file.read()
        st.subheader("AI-Generated Summary")
        st.text_area("Summary", summary_text, height=300)
    
        # download options 
        st.subheader("Download Summary")

        # txt download
        st.download_button(
            label="Download as TXT",
            data=summary_text,
            file_name=f"{topic_choice}_summary.txt",
            mime="text/plain"
        )
        # csv download
        df = pd.DataFrame({"Summary": [summary_text]})
        st.download_button(
            label="Download as CSV",
            data=df.to_csv(index=False).encode('utf-8'),
            file_name=f"{topic_choice}_summary.csv",
            mime="text/csv"
        )
    else:
        st.warning(f"No summary found for topic: {topic_choice}, run AI summarization first.")
        