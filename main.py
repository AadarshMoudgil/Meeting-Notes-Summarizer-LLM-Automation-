#!/usr/bin/env python3
"""
Meeting Notes Summarizer using LLM (OpenAI).
Reads transcript.txt → Summarizes → Outputs meeting_summary.md
"""

import os
import openai
import yaml

def load_config(path="config.yaml"):
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def read_transcript(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

def summarize_text(transcript, model="gpt-3.5-turbo"):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    if not openai.api_key:
        raise EnvironmentError("Please set OPENAI_API_KEY environment variable.")

    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant that summarizes meeting transcripts."},
            {"role": "user", "content": f"Summarize the following transcript into:\n1. Short summary\n2. Key points\n3. Action items (checklist).\n\nTranscript:\n{transcript}"}
        ],
        max_tokens=300
    )
    return response["choices"][0]["message"]["content"].strip()

def write_summary(output_file, summary):
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(summary)

def main():
    cfg = load_config()
    transcript = read_transcript(cfg["transcript_file"])
    print("📥 Transcript loaded")

    summary = summarize_text(transcript, cfg["model"])
    print("🤖 Summary generated")

    write_summary(cfg["output_file"], summary)
    print(f"✅ Summary saved to {cfg['output_file']}")

if __name__ == "__main__":
    main()
