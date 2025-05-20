# 🎓 Academic Chatbot using Flask

A production-ready academic chatbot built with Flask and NLTK. This chatbot understands academic slang (like "hw", "lect") and processes user queries using basic NLP techniques. Developed as part of a university software project with full documentation and test coverage.

---

## 📁 Project Structure

Banerjee_Dhonushree_102303592_Chatbot_Final/
├── 01-Project-management/ # Planning docs (timeline, risk, meetings)
├── 02-Requirements/ # Functional & non-functional specs
├── 03-Architecture/ # UML, system design, API specs
├── 04-Implementation/ # Source code, templates, tests


---

## 🚀 Features

- 🔍 **NLP-based query processing**
- 🤖 **Academic slang translation**
- 🧪 **Test coverage using Pytest**
- 🗂️ Modular Flask app structure
- 🎨 Clean frontend UI with chat and admin pages
- 📚 Full project documentation & sprint planning

---

## 🛠️ Setup Instructions

### 1. Clone the repository


git clone https://github.com/Dhonushree/flask-chatbot.git
cd Banerjee_Dhonushree_102303592_Chatbot_Final/04-Implementation

2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate     # Linux/macOS
venv\Scripts\activate        # Windows

3. Install dependencies
pip install -r requirements.txt

4. Download NLTK tokenizer data
import nltk
nltk.download('punkt')

5. Set environment variables
Create a .env file:

FLASK_APP=app
FLASK_ENV=development

6. Run the Flask app
flask run

Access the chatbot at: http://localhost:5000

💬 Sample Input & Output
Input Message	Bot Response
When is the hw due?	when is the homework due ?
Is lect cancelled?	is lecture cancelled ?

