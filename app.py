import streamlit as st
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Page configuration
st.set_page_config(page_title="AI Text Summarizer", page_icon="📝")

st.title("📝 Local AI Text Summarizer")
st.write("Summarize long text instantly using your offline **t5-small** model.")

# Cache model so it stays in RAM


@st.cache_resource
def load_model():
    model_name = "t5-small"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    return tokenizer, model


# Load model and tokenizer
with st.spinner("Loading local model into RAM..."):
    tokenizer, model = load_model()

# Input box
input_text = st.text_area("Paste your article or long text here:", height=220)

# Action button
if st.button("Generate Summary"):
    if not input_text.strip():
        st.warning("Please paste some text first!")
    else:
        with st.spinner("Generating summary..."):
            prompt = "summarize: " + input_text
            inputs = tokenizer(prompt, return_tensors="pt",
                               max_length=512, truncation=True)

            summary_ids = model.generate(
                inputs["input_ids"],
                max_length=80,
                min_length=25,
                num_beams=2,
                early_stopping=True
            )

            summary = tokenizer.decode(
                summary_ids[0], skip_special_tokens=True)

            st.subheader("Summary Output:")
            st.success(summary)
