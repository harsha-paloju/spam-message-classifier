from flask import Flask, render_template, request
import joblib
import os

app = Flask(__name__)

# Load model and vectorizer only once
model = joblib.load("spam_model.pkl")
cv = joblib.load("count_vectorizer.pkl")


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/result", methods=["POST"])
def result():

    message = request.form["message_text"]

    vector = cv.transform([message])

    prediction = model.predict(vector)[0]

    confidence = round(
        max(model.predict_proba(vector)[0]) * 100,
        2
    )

    return render_template(
        "result.html",
        answer=prediction,
        message=message,
        confidence=confidence
    )


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)