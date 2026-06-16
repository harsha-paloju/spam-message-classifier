# 📩 SMS Spam Classifier

A **Machine Learning-powered web application** that predicts whether an SMS message is **Spam** or **Not Spam** using a **Multinomial Naive Bayes classification model** and **CountVectorizer** for text feature extraction.

The application allows users to enter any SMS message through a simple web interface and instantly classifies it as **Spam 🚫** or **Not Spam ✅**.

---

## 🚀 Live Demo

>[ *(Add your Render deployment link here after deployment)*](https://spam-message-classifier-2-7s01.onrender.com/)

---

## 📸 Preview

### Home Page

- 📝 Enter or paste any SMS message.
- 🤖 Click **Check** to analyze the message.
- ⚡ Instantly predicts whether the message is Spam or Not Spam.

### Result Page

Displays:

- 📩 Entered SMS Message
- 🚫 Spam / ✅ Not Spam Prediction

---

# ✨ Features

- 🤖 Machine Learning-based SMS classification
- 📩 Detects Spam and Not Spam messages
- 🔤 Uses **CountVectorizer** for text preprocessing
- 🧠 Powered by **Multinomial Naive Bayes**
- ⚡ Fast Flask backend
- 🎨 Responsive and modern user interface
- 🌐 Easy to deploy on platforms like Render
- 📦 Pre-trained model loaded using Joblib

---

# 🧠 Machine Learning Model

### Algorithm Used

- **Multinomial Naive Bayes**

### Text Preprocessing

- CountVectorizer

The model is trained on an SMS Spam Collection dataset where messages are categorized into:

- **Spam**
- **Ham (Not Spam)**

The input message is converted into a numerical feature vector using **CountVectorizer** before prediction.

---

# 🛠 Tech Stack

### Backend

- Python
- Flask

### Machine Learning

- Scikit-learn
- Multinomial Naive Bayes
- CountVectorizer
- Joblib

### Frontend

- HTML5
- CSS3

---

# 📂 Project Structure

```text
sms_spam_classifier/
│
├── app.py
├── spam_model.pkl
├── count_vectorizer.pkl
├── requirements.txt
├── spam.csv
│
├── templates/
│   ├── home.html
│   └── result.html
│
├── static/
│   └── style.css
│
└── classifier.ipynb
```

---

# ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/sms_spam_classifier.git
```

Move into the project directory:

```bash
cd sms_spam_classifier
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the Flask application:

```bash
python app.py
```

Open your browser:

```
http://127.0.0.1:5000/
```

---

# 📊 Prediction Workflow

```text
User enters SMS
        │
        ▼
Flask Web Application
        │
        ▼
CountVectorizer
        │
        ▼
Feature Vector
        │
        ▼
Multinomial Naive Bayes Model
        │
        ▼
Prediction
        │
        ├── 🚫 Spam
        └── ✅ Not Spam
```

---

# 📦 Python Libraries Used

- Flask
- Scikit-learn
- Joblib
- NumPy
- Pandas
- SciPy
- Gunicorn

---

# 🎯 Future Improvements

- 📊 Display prediction confidence score using `predict_proba()`
- 🔗 Detect suspicious URLs and phishing links
- 🧹 Advanced text preprocessing (stemming and lemmatization)
- 🧠 Compare multiple machine learning models (SVM, Logistic Regression, Random Forest)
- 🌐 Build a REST API for integration with other applications
- 📱 Improve mobile responsiveness and UI/UX
- ☁️ Store prediction history using a database
- 🤖 Upgrade to Transformer-based NLP models for improved accuracy

---

# 👨‍💻 Author

**Harsha Paloju**

Aspiring AI Engineer passionate about Machine Learning, Flask, and building real-world AI applications.

If you like this project, don't forget to ⭐ **star the repository**!
