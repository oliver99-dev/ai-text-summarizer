# 📝 Local AI Text Summarizer

A lightweight, privacy-focused web application built with **Streamlit**, **Hugging Face Transformers (`t5-small`)**, and **PyTorch** that performs local text summarization directly on your machine without relying on external third-party API keys.

---

## 🚀 Key Features

- **Local Inference:** Utilizes the lightweight `t5-small` model from Hugging Face for fast, local text processing without sending data to external APIs.
- **Privacy-First Architecture:** Operates completely offline once model weights are cached locally.
- **Customizable Summary Parameters:** Adjust minimum and maximum summary length using interactive UI sliders.
- **Interactive Streamlit Interface:** Modern, user-friendly interface built for rapid document and paragraph summarization.
- **Virtual Environment Ready:** Easy configuration with standard Python tooling and virtual environments.

---

## 🛠️ Tech Stack

- **Frontend & Web Interface:** [Streamlit](https://streamlit.io/)
- **NLP / Machine Learning:** [Hugging Face Transformers](https://huggingface.co/docs/transformers/index) (`t5-small`)
- **Deep Learning Engine:** [PyTorch](https://pytorch.org/)
- **Version Control & Shell:** Git / Git Bash
- **IDE:** Visual Studio Code
- **Language & Runtime:** Python 3.10+

---

## 📂 Project Structure

```text
ai-text-summarizer/
├── .gitignore        # Excludes venv/, bytecode, and environment files
├── app.py            # Streamlit interface and T5 summarization pipeline
├── requirements.txt  # Project dependencies (transformers, torch, streamlit)
└── README.md         # Project documentation
