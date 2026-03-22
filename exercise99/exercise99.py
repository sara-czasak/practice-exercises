from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def get_notes():
    note = request.form['note']
    with open('notes_web_app.txt', 'a+') as file:
        file.write(f"{note}\n")
    return render_template('index.html')
