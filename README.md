# 🟦 Share n Care – Community Help Platform

A community-driven web platform that connects people who want to **offer** or **request** help in their locality.  
Designed with empathy and simplicity, Share n Care promotes small acts of kindness through an easy-to-use online portal.

---

## 🌍 Tech Stack
- **Backend:** Flask (Python)
- **Frontend:** HTML, CSS (Glassmorphism UI), Bootstrap, JS
- **Database:** SQLite

---

## 🧩 Project Structure

share-n-care/
│
├── app.py # Main Flask application
├── requirements.txt # Python dependencies
│
├── static/ # Static assets (CSS, JS, Images)
│ ├── css/
│ │ └── style.css # Custom styles
│ ├── js/
│ │ └── main.js # Interactive scripts
│ └── assets/
│ └── hero-bg.jpg # Background and visual assets
│
├── templates/ # HTML templates
│ ├── base.html # Common layout
│ ├── index.html # Homepage
│ ├── about.html # About page
│ ├── request_help.html # Help request page
│ └── contact.html # Contact page
│
└── README.md # Project overview and setup guide

## ⚙️ Setup Instructions
1. **Clone the repository**
    ```bash
   git clone https://github.com/yourusername/share-n-care.git
   cd share-n-care

2. **Create a virtual environment (optional but recommended)**
    ```bash
    python -m venv venv
    venv\Scripts\activate   # On Windows
    source venv/bin/activate   # On macOS/Linux

3. **Install dependencies**
    ```bash
    pip install -r requirements.txt

4. **Run the app**
    ```bash
    python app.py

5. **Open in browser**
    ```bash
    http://localhost:5000