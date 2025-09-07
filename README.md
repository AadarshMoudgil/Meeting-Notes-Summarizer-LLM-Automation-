# 📝 Meeting Notes Summarizer (AI Automation)

## What it is
A Python automation that converts **long meeting transcripts** into:
- Concise summary
- Bullet points
- Action items

## Client need
Business teams often record meetings but don't have time to read transcripts. They need a tool that generates summaries automatically.

## Solution
- Input: raw transcript text (`transcript.txt`)
- Processing: LLM API call (OpenAI or Hugging Face)
- Output: markdown summary (`meeting_summary.md`)

## Impact
- Saves hours of manual note-taking.
- Produces clean, shareable summaries.
- Can be extended into Slack/Email bots.

## Quick start
1. Install dependencies:
```bash
pip install -r requirements.txt
