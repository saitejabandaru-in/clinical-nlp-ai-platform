<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:141E30,100:243B55&height=200&section=header&text=NLP%20Clinical%20Notes%20Analyzer&fontSize=36&fontColor=E6EEF3&animation=fadeIn&fontAlignY=40" />

  <img src="https://img.shields.io/github/actions/workflow/status/saitejabandaru-in/clinical-nlp-ai-platform/python-app.yml?branch=main&label=Build&style=flat-square"/>
</p>

<p align="center">
  🏥 Clinical NLP &nbsp;|&nbsp; 🧠 Healthcare AI &nbsp;|&nbsp; 🔍 Text Intelligence
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?style=flat-square"/>
  <img src="https://img.shields.io/badge/NLP-spaCy-orange?style=flat-square"/>
  <img src="https://img.shields.io/badge/Transformers-HuggingFace-yellow?style=flat-square"/>
  <img src="https://img.shields.io/badge/NER-SciSpaCy%20%7C%20BioBERT-green?style=flat-square"/>
  <img src="https://img.shields.io/badge/API-FastAPI-red?style=flat-square"/>
  <img src="https://img.shields.io/badge/Visualization-Plotly-brightgreen?style=flat-square"/>
</p>

---

# 🏥 NLP Clinical Notes Analyzer

An **NLP-powered clinical intelligence system** for transforming **unstructured medical notes into structured, actionable insights**.

This project demonstrates how **modern healthcare AI pipelines combine NLP, explainability, and clinical coding systems** to support decision-making.

---

## 🧠 Overview

The system processes clinical narratives to:

- Extract structured medical entities  
- Analyze patient outcome sentiment  
- Discover hidden topics in clinical text  
- Suggest ICD-10 diagnosis codes  
- Ensure privacy through PHI de-identification  

Built to mirror **real-world clinical NLP systems used in hospitals, EHR platforms, and research pipelines**.

---

## ✨ Core Features

### 🧬 Clinical NER
- Extracts:
  - Medications  
  - Diagnoses  
  - Procedures  
  - Anatomical entities  
- Powered by SciSpaCy + BioBERT  

### 📊 Sentiment Analysis
- Detects:
  - Positive outcomes  
  - Neutral observations  
  - Negative / critical conditions  
- Tracks sentiment across patient timelines  

### 🧠 Topic Modeling
- LDA and BERTopic clustering  
- Identifies clinical themes and specialties  

### 🔑 Keyword Extraction
- TF-IDF and RAKE algorithms  
- Highlights key clinical phrases  

### 🏷 ICD-10 Code Suggestion
- Maps extracted entities to diagnosis codes  
- Supports automated clinical documentation  

### 🔒 De-Identification (HIPAA)
- Detects and removes:
  - Names  
  - Dates  
  - Medical record numbers  
- Ensures privacy compliance  

### ☁️ Interactive Word Cloud
- Real-time visualization of clinical terminology  
- Weighted by frequency and relevance  

---

## 🧬 System Workflow

```
Clinical Notes (Unstructured Text)
↓
Preprocessing (Cleaning + De-identification)
↓
NLP Pipeline (NER + Sentiment + Topics)
↓
Feature Extraction (Keywords + Entities)
↓
ICD Code Mapping
↓
Visualization (Word Cloud + Trends)
↓
API Output (Structured Insights)
```

---

## 🏗 Project Structure

```

nlp-clinical-notes-analyzer/

├── models/
│   ├── ner/
│   │   ├── clinical_ner_model.py
│   │   └── entity_linker.py
│   ├── sentiment/
│   │   ├── clinical_sentiment.py
│   │   └── aspect_sentiment.py
│   ├── topic/
│   │   ├── lda_model.py
│   │   └── bertopic_model.py
│   └── coding/
│       └── icd10_classifier.py

├── preprocessing/
│   ├── tokenizer.py
│   ├── section_splitter.py
│   └── deidentifier.py

├── visualization/
│   ├── word_cloud.py
│   ├── sentiment_timeline.py
│   └── topic_radar.py

├── api/
│   └── serve.py

├── config/
│   └── model_config.yaml

├── tests/
├── requirements.txt
└── README.md

```

---

## 🚀 Quick Start

### Clone repository
```bash
git clone https://github.com/saitejabandaru-in/clinical-nlp-ai-platform.git
cd clinical-nlp-ai-platform
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run analysis

```bash
python -m clinical_nlp_ai_platform --input data/sample_note.txt --pretty
```

### Run API

```bash
uvicorn api.serve:app --reload
```

Then call `POST /analyze` with a JSON body such as:

```json
{
  "text": "Patient has diabetes and hypertension. Metformin is tolerated."
}
```

> This repository is an engineering demo, not a medical device or clinical decision system. Outputs should be reviewed by qualified professionals before any real-world use.

---

## 📊 Modules

| Module         | Description                          |
| -------------- | ------------------------------------ |
| Clinical NER   | Extracts drugs, diseases, procedures |
| Sentiment      | Classifies clinical outcome tone     |
| Topic Clusters | Groups notes by medical themes       |
| Keyword Cloud  | Visualizes key clinical terms        |
| ICD Coding     | Suggests ICD-10 codes                |
| De-ID          | Removes PHI for compliance           |

---

## 🧪 Tech Stack

| Layer             | Tools                            |
| ----------------- | -------------------------------- |
| NLP Framework     | spaCy, Hugging Face Transformers |
| NER               | SciSpaCy, MedCAT, BioBERT        |
| Sentiment         | RoBERTa (fine-tuned)             |
| Topic Modeling    | BERTopic, Gensim                 |
| De-identification | Presidio                         |
| Visualization     | Plotly, Matplotlib               |
| API               | FastAPI                          |

---

## 📈 What This Project Demonstrates

✔ Clinical NLP pipeline design
✔ Named Entity Recognition (NER) in healthcare
✔ Explainable AI in medical text
✔ Topic modeling on clinical data
✔ Privacy-preserving NLP (HIPAA compliance)
✔ End-to-end AI system deployment

---

## 👨‍💻 Author

**Sai Teja Bandaru**
*Data Scientist & Healthcare AI Engineer*

🌐 Portfolio
💼 LinkedIn
💻 GitHub

---

## 📄 License

MIT License — see `LICENSE` for details.

---

## ⭐ Support

If you find this useful:

⭐ Star the repo
🍴 Fork it
📢 Share it

---

> Turning clinical text into structured intelligence for better healthcare decisions.


## Contributing

Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/amazing-feature`).
3. Run tests before committing.
4. Push to the branch (`git push origin feature/amazing-feature`).
5. Open a Pull Request.
