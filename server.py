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

@app.route('/show_one_user/<id>')
def one_user(id):
    data = {
        'user_id' : id
    }
    one_user = User.one_user(data)
    print(one_user)
    return render_template('one_user.html', user = one_user)

@app.route('/show_update_user/<id>')
def show_update_user_page(id):
    data = {
        'user_id' : id
    }
    show_update_user = User.show_update_user_page(data)
    return render_template('update_user.html', user = show_update_user)

@app.route('/update_user/<id>', methods=['POST'])
def update_user(id):
    data = {
        'user_id' : id,
        'fname': request.form['fname'],
        'lname': request.form['lname'],
        'email': request.form['email']
    }
    User.update_user(data)
    return redirect('/show_users')

@app.route('/delete_user/<id>', methods=['POST'])
def delete_user(id):
    data = {
        'user_id' : id
    }
    User.delete_user(data)
    return redirect('/show_users')

@app.route('/return_to_create')
def return_to_create():
    return render_template('index.html')

@app.route('/return_to_users')
def return_to_users():
    return redirect('/show_users')

if __name__=='__main__':
    app.run(debug=True)