# 🛍️ Automated Customer Support Workflow with GPT & LangGraph

This project is an **AI-powered customer support assistant** that listens to natural language queries and responds accordingly. It uses **OpenAI GPT-4o-mini** to classify customer questions and **LangGraph** to route them through predefined support logic.

---

## ✨ Features

- 🔊 Accepts customer queries via text (can be extended to voice)
- 🧠 Classifies questions into categories using GPT
- 🔁 Routes queries using LangGraph based on intent
- 📬 Responds with helpful, predefined answers
- 🛠 Easily extendable for more use cases

---

## 🌐 LangGraph Workflow
```
START
  ↓
classify_query
  ├─▶ order_status     ─▶ END
  ├─▶ return_policy    ─▶ END
  ├─▶ product_info     ─▶ END
  └─▶ other            ─▶ END

```
---
## 💡 Use Cases

This assistant helps automate responses for:

- 📦 **Order Status**  
- 🔁 **Return Policy**  
- 🛍️ **Product Information**  
- ❓ **Other General Inquiries**

---

## 🗂️ Project Structure

```
.
├── test.py # LangGraph workflow and logic
├── .env # API keys and secrets
├── requirements.txt # Python dependencies
├── README.md # You're reading it!
```
---

## 🧠 How It Works

1. A user enters a query like "Where is my package?"
2. GPT classifies it as `order_status`
3. LangGraph routes it to the correct handler
4. Assistant replies:  
   `You can track your order here: https://store.com/track-order`

---

## 🧪 Demo
```
Customer: Can I return my shoes?
Agent: Our return policy is available here: https://store.com/returns
(Detected Type: return_policy)
```

---
## ✅ Requirements

- Python 3.9+
- OpenAI API key

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-org/AI-Voice-Assistant-using-OpenAI-LangGraph-Checkpointer.git
cd AI-Voice-Assistant-using-OpenAI-LangGraph-Checkpointer
```
### 2. Set up environment
```bash
pip install -r requirements.txt
```

### Create a .env file:
```
OPENAI_API_KEY=your-openai-api-key
```
## 🚀 Run the Assistant
```
python test.py
```