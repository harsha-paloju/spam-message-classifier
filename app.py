from flask import Flask,request,render_template
import joblib
app=Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/result",methods=["POST","GET"])
def result():
    model=joblib.load("spam_model.pkl")
    cv=joblib.load("count_vectorizer.pkl")
    
    message = request.form["message_text"]

    vector = cv.transform([message])

    prediction = model.predict(vector)[0]

    return render_template(

        "result.html",

        answer=prediction,

        message=message

    )

app.run(debug=True)