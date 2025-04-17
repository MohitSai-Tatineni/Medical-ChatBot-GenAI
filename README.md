# CAREPAL: AI-Driven Health & Activity Partner

## 🧠 Problem Statement
Many individuals struggle to navigate overwhelming and often conflicting online health information. CAREPAL addresses this by delivering **personalized, evidence-based wellness guidance** through a chatbot that simplifies medical content into actionable lifestyle recommendations.

--

## 🚀 Project Overview
CAREPAL is a generative AI-powered chatbot that provides health and wellness recommendations based on reliable guidelines from the **WHO**, **CDC**, and **US Department of Health Services**. It uses the **Llama 2 language model** and semantic search to deliver context-aware, non-diagnostic advice.

--

## Steps to Run the Project

### 1. Create a Conda Environment
```bash
conda create -n mchatbot python=3.8 -y
```

### 2. Activate the Conda Environment
```bash
conda activate mchatbot
```
### 3. Install the requirements

```bash
pip install -r requirements.txt
```

### Create a `.env` file in the root directory and add your Pinecone credentials as follows:

```ini
PINECONE_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
PINECONE_API_ENV = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```
### Download the quantized model from the link provided in model folder & keep the model in the model directory:

```ini
## Download the Llama 2 Model:

llama-2-7b-chat.ggmlv3.q4_0.bin

## From the following link:
https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/tree/main

```

## Description
This project demonstrates the creation of an end-to-end medical chatbot using Llama2. The chatbot leverages advanced language models to retrieve and answer medical queries based on contextually relevant data.

## Prerequisites
- Python 3.8
- Conda
- Access to required API keys (Pinecone, OpenAI)
- Additional dependencies installed in the created environment

## How to Use
1. Follow the steps above to set up the environment.
2. Run the project script as described in the project documentation or scripts folder.

--

## 🛠️ Tech Stack

| Layer           | Technologies Used                    |
|----------------|--------------------------------------|
| Frontend       | React.js                             |
| Backend        | Flask (Python)                       |
| LLM            | Meta's Llama 2                       |
| Embeddings     | OpenAI Embedding Models              |
| Vector DB      | Pinecone                             |
| NLP Libraries  | SpaCy, NLTK                          |
| Deployment     | Localhost / Streamlit (optional)     |

---

## 📚 Dataset Sources

- [WHO Guidelines on Physical Activity](https://apps.who.int/iris/bitstream/handle/10665/336656/9789240015128-eng.pdf)
- [CDC Physical Activity Guidelines](https://health.gov/sites/default/files/2019-09/Physical_Activity_Guidelines_2nd_edition.pdf)
- Dietary Guidelines for Americans 2020–2025
- Curated datasets from public health repositories

--

## 🧩 Approach Used

1. **Text Preprocessing**: Cleaned and chunked static documents into ~200 token segments.
2. **Embedding Generation**: Used OpenAI models to create dense vector representations.
3. **Semantic Indexing**: Indexed documents in Pinecone for similarity search.
4. **Query Resolution**: Retrieved relevant context and fed it into Llama 2 for response generation.
5. **Integration**: Combined all parts into a Flask backend with a React frontend UI.

--

## 🧠 Model Information

- **Llama 2-7B Chat** (quantized version)
- Token context limit: 4096
- Real-time, RAG-enabled conversational response generation
- Non-diagnostic, personalized wellness responses

--

## 📊 Application Results

- Delivered responses with < 2s latency
- Provided personalized advice based on user inputs (age, lifestyle, concerns)
- Adhered to public health standards without compromising on usability

--

## 🧱 Application Architecture

> 📌 *Paste architecture diagram image here*

--

## 📈 Future Enhancements

- Multilingual support
- Wearable device integration (e.g., Fitbit, Apple Health)
- Expansion of data sources
- Real-time sentiment adaptation

--

## 👨‍💻 Authors

- Dhyey Joshi
> Sponsored by **Crisis Technologies Innovation Lab** – Fall 2024

## 📝 License

This project is licensed under the [MIT License](LICENSE).


