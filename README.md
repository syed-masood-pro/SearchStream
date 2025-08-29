# SearchStream: A LangChain Chatbot with Multi-Tool Search

![Status](https://img.shields.io/badge/Status-Complete-brightgreen)
![License](https://img.shields.io/badge/License-MIT-blue.svg)
![Framework](https://img.shields.io/badge/Framework-Streamlit-FF4B4B?logo=streamlit)
![LLM](https://img.shields.io/badge/LLM-Groq%20%7C%20LangChain%20%7C%20Llama_3-blueviolet)
![Language](https://img.shields.io/badge/Language-Python_3.11-yellow?logo=python)  

## 📝 Table of Contents
- [📌 About the Project](#-about-the-project)
- [✨ Key Features](#-key-features)
- [🛠️ Requirements](#️-requirements)
- [🚀 How to Run](#-how-to-run)
- [🖼️ Sample Interface](#-sample-interface)
- [📄 License](#-license)
- [📧 Contact](#-contact)
---
## 📌 About the Project

This project is an intelligent chatbot built with Streamlit and powered by **Groq's** high-speed inference for the **Llama 3** model. It leverages a **LangChain** agent equipped with multiple tools, allowing it to search the web with DuckDuckGo, query academic papers on Arxiv, and look up information on Wikipedia to answer a wide range of user questions.

---

## ✨ Key Features
  * **High-Speed Inference:** Utilizes Groq's low-latency engine for near-instantaneous responses from the Llama 3 model.
  * **Multi-Tool Agent:** Can dynamically choose the best tool for a query, whether it's a general web search, an academic question, or a factual lookup.
  * **Search Capabilities:** Integrates DuckDuckGo, Arxiv, and Wikipedia for comprehensive information retrieval.
  * **Interactive UI:** A clean and simple chat interface built with Streamlit, including real-time thought processes of the agent.
  * **Secure API Handling:** API keys are entered through a secure Streamlit password input in the sidebar.
  
---
## 🛠️ Requirements

You can install all necessary Python packages by running the following command:

```bash 
pip install -r requirements.txt
```
---

## 🚀 How to Run

**1. Clone the Repository**
```
git clone https://github.com/syed-masood-pro/SearchStream.git
cd SearchStream
```

**2. Install Dependencies**
```
pip install -r requirements.txt
```

**3. Get Your API Keyt**

You will need a free API key from [Groq](https://console.groq.com/keys).

**4. Run the Streamlit App**

From your terminal, run the following command to start the application (assuming your file is named `app.py`):
```bash
streamlit run app.py
```
The app will open in your web browser. To start interacting with the chatbot, enter your Groq API key in the sidebar.

---

## 🖼️ Sample Interface

Below is an example of the chatbot interface. The main window displays the conversation, while the sidebar is used for API key configuration.

<img width="959" height="475" alt="proj1" src="https://github.com/user-attachments/assets/a505d7d1-a2c2-485a-89cf-f27f725b0e8f" />
<img width="959" height="475" alt="proj2" src="https://github.com/user-attachments/assets/bc945f67-5334-4a3b-9fb5-02cd00bf847a" />
<img width="959" height="474" alt="proj3" src="https://github.com/user-attachments/assets/9961f278-de16-48a4-9b8f-c560f2e55663" />


---

## 📄 License

This project is licensed under the MIT License.

---

## 📧 Contact
**Syed Masood**

✉️ [syedmasood.pro@gmail.com](syedmasood.pro@gmail.com)

🔗 [GitHub Profile](https://github.com/syed-masood-pro/)

💼 [LinkedIn](https://www.linkedin.com/in/syed-masood-pro/)
