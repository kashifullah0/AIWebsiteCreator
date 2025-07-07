# AI Web Designer

Generate a complete website (HTML, CSS, JS) from one prompt using Streamlit, OpenAI Agents SDK, and Gemini API.

---

## 🗂️ Project Files

- `app.py` → Main Streamlit app  
- `.env` → Store `GOOGLE_API_KEY`  
- `requirements.txt` → Dependencies  
- `preview.html` → Generated website (auto-created)

---

## ⚙️ Tech Stack

- Python 3.12+
- Streamlit
- OpenAI Agents SDK
- Gemini API
- uv (Python package manager)
- dotenv

---

## 🚀 Setup & Run

```bash
# Clone repo
git clone https://github.com/yourusername/ai-web-designer.git
cd ai-web-designer

# Create & activate venv
uv venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows

# Install dependencies
uv pip install -r requirements.txt

# Add .env
# File: .env
GOOGLE_API_KEY=your_gemini_api_key_here

# Run app
streamlit run app.py
