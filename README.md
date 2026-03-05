# 📚 Gibberish Children's Stories

A fun Streamlit chat app for generating tiny story continuations with `roneneldan/TinyStories-1M` on Hugging Face.

## ✨ What it does
- Lets you chat with a small storytelling model
- Streams generated text in the UI
- Includes controls for `max_new_tokens`, `temperature`, and `top_p`

## 🔐 Hugging Face token required
You need a Hugging Face access token to download the model from Hugging Face Hub.

1. Create a token in your Hugging Face account (`hf_...`).
2. Add it to `.streamlit/secrets.toml`:

```toml
HF_TOKEN = "hf_your_token_here"
```

The app reads this via `st.secrets` (`secrets["HF_TOKEN"]`).

## ⚙️ Setup
```powershell
pip install -r requirements.txt
```

## ▶️ Run
```powershell
streamlit run streamlit_app.py
```

Or use the `Run and Debug` sidebar if you are on VSCode.

## 🧱 Tech stack
- Python
- Streamlit
- Hugging Face Transformers
- PyTorch + Accelerate
