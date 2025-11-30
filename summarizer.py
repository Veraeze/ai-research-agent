# summarizer.py
# 1. Load raw text from /data folder
# 2. Split into chunks if too large
# 3. Send to AI model for summarization
# 4. Return a clean summary

from transformers import pipeline
import os

# Step 1: Initialize the summarization pipeline
# This loads the local HuggingFace model for summarization
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def summarize_file(input_file, output_file):
    """
    Summarizes a text file and saves the result.
    
    input_file: str -> path to scraped text file
    output_file: str -> path to save summary
    """
    # Step 2: Read the raw text
    with open(input_file, "r", encoding="utf-8") as f:
        text = f.read()

    # Step 3: Chunk the text if it's too long (model has max token limit)
    max_chunk_size = 1000  # roughly 1000 words
    text_chunks = [text[i:i+max_chunk_size] for i in range(0, len(text), max_chunk_size)]

    summaries = []
    # Step 4: Summarize each chunk
    for chunk in text_chunks:
        summary = summarizer(chunk, max_length=150, min_length=50, do_sample=False)[0]['summary_text']
        summaries.append(summary)

    # Step 5: Combine all chunk summaries into one
    final_summary = "\n".join(summaries)

    # Step 6: Ensure output folder exists
    os.makedirs("output", exist_ok=True)

    # Step 7: Save final summary
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(final_summary)

    print(f" Summary saved to {output_file}")

# Optional: Run all scraped files at once
def summarize_all():
    files = ["data/wikipedia.txt", "data/ibm.txt", "data/nature.txt"]
    for file in files:
        output_name = f"output/{os.path.basename(file).replace('.txt','_summary.txt')}"
        summarize_file(file, output_name)