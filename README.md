# 🍔 FoodSnap Nutrition – AI-powered Nutrition Analyzer

**FoodSnap Nutrition** is a Streamlit-based web application that allows users to upload a **photo of any food** and instantly get its **nutritional breakdown** – powered by **Google Gemini Vision** for image understanding and **Calories Ninja API** for nutritional data.

---

## 🚀 Features

- 📷 **Upload Food Image** – Supports JPEG/PNG formats  
- 🧠 **AI-powered Food Recognition** – Uses **Gemini 1.5 Flash** to detect the food item  
- 🍽 **Accurate Nutrition Facts** – Calories, proteins, fats, carbs, etc.  
- ⚡ **Fast & Lightweight** – Runs entirely in your browser with Streamlit  
- 🔒 **Secure API Keys** – Stored in `.env`, never exposed in code  

---

## 🖼 Demo

*(Replace this with a real screenshot later)*

![Demo Screenshot](docs/demo_screenshot.png)

---

## 🗂 Project Structure

foodsnap-nutrition/
│
├── .env                 # API keys (never push to GitHub)
├── .gitignore           # Ignore .env and unnecessary files
├── app.py               # Streamlit app entry point
├── config.py            # Loads API keys and settings
├── requirements.txt     # Dependencies
├── services/
│   ├── __init__.py
│   ├── gemini_service.py       # Image recognition via Gemini
│   └── nutrition_service.py    # Nutrition lookup via Calories Ninja
└── utils/
    ├── __init__.py
    └── image_utils.py          # Image handling helpers


## 🔑 Setup & Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/foodsnap-nutrition.git
   cd foodsnap-nutrition
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Create .env file in the project root:

env
Copy
Edit
GEMINI_API_KEY=your_gemini_api_key_here
CALORIES_NINJA_KEY=your_calories_ninja_key_here
Run the app

bash
Copy
Edit
streamlit run app.py
⚙️ Tech Stack
Frontend & Backend – Streamlit

Image Recognition – Google Gemini AI

Nutrition Data – Calories Ninja API

Environment Management – python-dotenv

💡 How it Works
User uploads an image

Gemini AI analyzes the food and predicts its name

Calories Ninja API fetches nutrition details

The app displays a clean nutrition facts table

📌 Future Improvements
Support for multiple foods in one image

More precise portion size detection

Save nutrition history for logged-in users

Mobile-friendly PWA version

📜 License
MIT License – Feel free to use and modify for your own projects.

🙌 Acknowledgements
Google Gemini AI for image recognition

Calories Ninja for nutrition database

Streamlit for a simple yet powerful UI framework
