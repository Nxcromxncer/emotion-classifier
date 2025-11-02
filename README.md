# 🌌 Emovera – Emotion Intelligence for Customer Experience  
> _Because feedback is more than ratings — it's emotion._

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Streamlit](https://img.shields.io/badge/Framework-Streamlit-red)
![NLP](https://img.shields.io/badge/AI-NLP%20%7C%20Emotion%20Classification-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 📌 Overview  

**Emovera** is an AI-powered application that analyzes customer comments and classifies them based on **emotions instead of numeric ratings**.  
Traditional metrics like CSAT or star ratings only measure satisfaction, but **they do not explain how customers actually feel**.

Emovera bridges this gap by detecting emotional states from customer feedback such as:

| Emotion | Emoji |
|---------|-------|
| Happy | 😄 |
| Neutral | 😐 |
| Angry | 😡 |
| Sad | 😢 |
| Surprised | 😮 |
| Trust | 🤝 |
| Confusion | 😕 |
| Regret | 😔 |
| Love | ❤️ |

This enables businesses to make **human-centered decisions**, track emotional trends, and improve customer experience based on **real emotional insights** — not just numbers.

---

## ✨ Key Features

✅ AI-powered emotion classifier (multi-label)  
✅ Upload CSV / text file and auto-analyze comments  
✅ Modern Glassmorphism UI in Streamlit  
✅ Real-time emotion detection and visualization  
✅ Interactive dashboard with statistics & charts  
✅ Downloadable emotion-labeled output  
✅ Page tracking system + analytics log  
✅ Supports both single comment input & batch mode  

---

## 🧠 How It Works

1. User enters text (or uploads CSV)
2. NLP model processes the input
3. The system predicts emotional class from 8–10 labels
4. Results appear in UI with:
   - Emotion tag
   - Probability score
   - Emoji visualization
5. Download results as CSV for further use

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|------------|
| Frontend | Streamlit + Custom CSS (Glass UI) |
| Backend | Python |
| ML Model | Scikit-learn / Transformers (custom trained) |
| Data | Preprocessed customer review dataset |
| Logging | SQLite / CSV logs |
| Deployment | Streamlit Cloud / Local runtime |

---

## 📂 Project Structure

