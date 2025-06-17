from flask import Flask, render_template, request
from function import count_words # type: ignore

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    word_count = None
    if request.method == "POST":
        text = request.form.get("text")
        word_count = count_words(text)
    return render_template("index.html", word_count=word_count)

if __name__ == "_main_":
    app.run(debug=True)