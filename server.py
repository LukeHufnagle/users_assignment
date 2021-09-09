from flask import Flask, render_template, redirect, request, session
from user import User
app = Flask(__name__)
app.secret_key = "Its a secret"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/show_users')
def show_users():
    users = User.select_all_users()
    return render_template('show.html', users = users)


@app.route('/create_user', methods=["POST"])
def create_new_user():
    data = {
        'fname': request.form['fname'],
        'lname': request.form['lname'],
        'email': request.form['email']
    }
    User.create_user(data)
    return redirect('/show_users')




if __name__=='__main__':
    app.run(debug=True)