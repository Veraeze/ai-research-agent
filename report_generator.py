import os
from datetime import datetime

def generate_combined_report(summary_folder="output", report_file="output/final_research_report.txt"):
    """
    Combines all summary files into one single research report with timestamps.
    
    summary_folder: str -> folder containing *_summary.txt files
    report_file: str -> path to save the combined report
    """

    # Step 1: Ensure the output folder exists
    os.makedirs(os.path.dirname(report_file), exist_ok=True)

    # Step 2: Get all summary files in the folder
    summary_files = [f for f in os.listdir(summary_folder) if f.endswith("_summary.txt")]
    
    # Step 3: Sort files alphabetically (optional)
    summary_files.sort()

    # Step 4: Initialize combined report content
    combined_content = f"AI Research Agent Report\nGenerated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"

    # Step 5: Read each summary file and append
    for file_name in summary_files:
        combined_content += f"--- {file_name} ---\n"
        with open(os.path.join(summary_folder, file_name), "r", encoding="utf-8") as f:
            combined_content += f.read() + "\n\n"

    # Step 6: Save the combined report
    with open(report_file, "w", encoding="utf-8") as f:
        f.write(combined_content)

    print(f" Combined research report saved to {report_file}")


if __name__ == "__main__":
    generate_combined_report()