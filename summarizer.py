import sys
import textwrap
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

print("=" * 50)
print("     FAST AI TEXT SUMMARIZER (t5-small)")
print("=" * 50)
print("Loading model into memory, please wait...\n")

MODEL_NAME = "t5-small"

# Load tokenizer and model directly without using pipeline task aliases
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)

print("--> Model loaded successfully!\n")

print("Paste or type your text below (press Enter, then Ctrl+Z, then Enter to finish):")
input_text = sys.stdin.read().strip()

if not input_text:
    print("\nError: No text provided to summarize.")
    sys.exit()

print("\nGenerating summary...")

# Format prompt and tokenize input
prompt = "summarize: " + input_text
inputs = tokenizer(prompt, return_tensors="pt",
                   max_length=512, truncation=True)

# Generate summary tokens
summary_ids = model.generate(
    inputs["input_ids"],
    max_length=60,
    min_length=20,
    num_beams=2,
    early_stopping=True
)

# Decode output back into text
raw_summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

print("\n" + "=" * 50)
print("SUMMARY OUTPUT:")
print("=" * 50)
print(textwrap.fill(raw_summary, width=70))
print("=" * 50)
