from flask import Flask, render_template, request
import os

app = Flask(__name__, template_folder='templates')


@app.route("/")
def hello():
    return render_template("UI.html")


@app.route("/", methods=['GET', 'POST'])
def my_form_post():
    text = request.form['text']
    processed_text = text.lower()
    return (os.popen(f'python3 slash.py {processed_text}')).read()


if __name__ == '__main__':
    """
    Execution starts here.
    """
    app.run()
