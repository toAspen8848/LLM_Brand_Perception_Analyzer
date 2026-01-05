# 🤖 LLM Brand Perception Analyzer

A Streamlit-based tool that queries open-weight LLMs (like LLaMA3 or Mistral via Ollama) to analyze **how brands are perceived by AI models**. It extracts brand mentions and rationales from LLM responses and applies **sentiment analysis** to understand the tone of those mentions — giving you a clear view of brand perception through the lens of modern AI.

---

## 🎯 Features

- 🔍 Query local LLMs (via [Ollama](https://ollama.com)) for brand recommendations
- 🧠 Extract brand names and reasons using pattern matching
- ❤️ Run sentiment analysis on brand descriptions using `TextBlob`
- 📊 Visualize sentiment scores via interactive bar charts
- 🧾 See a text summary of each brand and its perceived value

---

## 📂 Project Structure

```
llm-brand-analyzer/
├── app/
│   ├── query_llm.py       # Querying LLMs via Ollama
│   ├── extract.py         # Extract brand:reason pairs
│   ├── sentiment.py       # TextBlob-based sentiment scoring
│   ├── visualize.py       # Streamlit & Plotly visualization
├── main.py                # Streamlit app entrypoint
├── requirements.txt       # All Python dependencies
└── README.md              # Project overview and usage
```

---

## 🚀 How to Run Locally

### 1. Clone the Repo
```bash
git clone https://github.com/your-username/llm-brand-analyzer.git
cd llm-brand-analyzer
```

### 2. Create & Activate Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

### 3. Install Requirements
```bash
pip install -r requirements.txt
python -m textblob.download_corpora
```

### 4. Install & Run Ollama
Install Ollama from [https://ollama.com](https://ollama.com)

```bash
ollama pull mistral  # or llama3, gemma, etc.
ollama run mistral
```

### 5. Start the Streamlit App
```bash
streamlit run main.py
```

---

## 🧪 Sample Prompt

> *"What are the top 2 brands in the luxury clothing industry and why are they popular?"*

### Output:
- **Louis Vuitton**: *Sentiment: 0.34*

Louis Vuitton is a French fashion house and luxury retail company founded in 1854 by Louis Vuitton. The brand is incredibly popular due to its rich history, high-quality craftsmanship, timeless designs, and innovative approach to luxury goods. Louis Vuitton's trademark monogram canvas, elegant leather goods, and iconic handbags have become status symbols worldwide. The brand has expanded beyond luggage, clothing, shoes, watches, jewelry, accessories, and more, maintaining a consistent level of quality and exclusivity that continues to attract consumers.


- **Gucci**: *Sentiment: 0.0*

Guccio Gucci founded the Italian luxury brand

---

## 🛠 Tech Stack

| Layer      | Tools                              |
|------------|------------------------------------|
| Frontend   | Streamlit                          |
| Backend    | Python                             |
| LLMs       | Ollama + Mistral / LLaMA3 (local)  |
| NLP        | TextBlob for sentiment analysis    |
| Charts     | Plotly for visualizations          |


---

## 📜 License

MIT License


