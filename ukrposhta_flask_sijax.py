from datetime import datetime
from flask import request, Flask, render_template, url_for, redirect, session
from sqlalchemy import Column, create_engine, String, ForeignKey, Date
from sqlalchemy.orm import DeclarativeBase, sessionmaker, Mapped, mapped_column
from flask import request, Flask, render_template, url_for, redirect, session, jsonify
from flask_mail import Mail, Message

from config import MAIL, MAIL_PASSWORD

app = Flask(__name__)
app.config['SECRET_KEY'] = '12212112'
app.config["PERMANENT_SESSION_LIFETIME"]

app.config['MAIL_SERVER'] = 'smtp.ukr.net'

app.config['MAIL_PORT'] = 465

app.config['MAIL_USERNAME'] = MAIL

app.config['MAIL_PASSWORD'] = MAIL_PASSWORD

app.config['MAIL_DEFAULT_SENDER'] = MAIL

app.config['MAIL_USE_TLS'] = False

app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

app.app_context().push()

@app.route('/')
def f_1():
    return render_template('ukrposhta_home_sijax.html')

@app.route('/give_signup')
def f_2():
    return render_template('ukrposhta_signup_sijax.html')

@app.route('/give_login')
def f_3():
    return render_template('ukrposhta_login_sijax.html')

@app.route('/signup', methods=['POST'])
def f_2_2():
    data = request.form['username']
    print(data)

    user_email = 'ilyalisenko12@gmail.com'
    email_message = Message('Test', recipients=[user_email])
    email_message.body = 'text'

    mail.send(email_message)

    response_data = {'message': 'Ви зареєстровані'}
    return jsonify(response_data), 200

@app.route('/signup', methods=['POST'])
def f_2_2():
    data = request.form['username']
    print(data)

    response_data = {'message': 'Ви увійши в акаунт'}
    return jsonify(response_data), 200


if __name__ == "__main__":
    app.run(debug=True, port=8000)
