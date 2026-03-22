from flask import Flask, render_template, request
import string


with open('users.txt', 'r') as file:
    data = file.readlines()
    users = [data.strip() for data in data]


def check_if_exists(user):
    if user.capitalize() == user:
        return True
    else:
        return False


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def check_form():
    username = request.form['username']
    password = request.form['password']
    taken = check_if_exists(username)
    if not taken:
        min_length = 5
        uppercase_list = list(string.ascii_uppercase)
        numbers_list = list(string.digits)
        long_enough = False
        has_upper = False
        has_num = False

        if len(password) >= min_length:
            long_enough = True
            for char in password:
                if char in uppercase_list:
                    has_upper = True
                    for char2 in numbers_list:
                        if char2 in password:
                            has_num = True

                            return "<p>Password created sucessfully!</p>"
    return render_template('index.html', username=username)

