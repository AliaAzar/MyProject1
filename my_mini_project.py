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

engine = create_engine("sqlite:///my_mini_project.db", echo=True)
Session = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    def create_db(self):
        Base.metadata.create_all(engine)

    def drop_db(self):
        Base.metadata.drop_all(engine)

class Users(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(80))
    email: Mapped[str] = mapped_column(String(80))
    password: Mapped[str] = mapped_column(String(80))

class Answers(Base):
    __tablename__ = "answers"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    answer1: Mapped[str] = mapped_column(String(80))
    answer2: Mapped[str] = mapped_column(String(80))
    answer3: Mapped[str] = mapped_column(String(80))
    answer4: Mapped[str] = mapped_column(String(80))
    answer5: Mapped[str] = mapped_column(String(80))
    answer6: Mapped[str] = mapped_column(String(80))
    answer7: Mapped[str] = mapped_column(String(80))
    answer8: Mapped[str] = mapped_column(String(80))
    answer9: Mapped[str] = mapped_column(String(80))
    answer10: Mapped[str] = mapped_column(String(80))

# base = Base()
# base.create_db()


user_answers_list = []
my_answers_list = ["Суші", "Мохіто", "Болгарський перець, капуста Кольрабі, редиска",
                   "Яблуко, гранат, помело, мандаринки", "Огірок, полуниця, кавун, виноград", "Літо",
                   ["Гроза зі зливою", "Швидкий товстий сні", "Похмуро", "Легкий дощ"], "7", "13",
                   ["Математика", "Фізика", "Англійська мова", "Німецька мова", "Інша зарубіжна мова"]]
similarity = 0


@app.route("/")
def f_1():
    return render_template("test_home_sijax.html")

@app.route("/login_pg")
def f_2():
    return render_template("test_login_sijax.html")

@app.route("/login", methods=["POST"])
def f_2_2():
    name = request.form["name"]
    password = request.form["password"]
    with Session() as session1:
        user = session1.query(Users).filter_by(name=name, password=password).first()
    if user:
        data = {"message": "Ви успішно війшли в аккаунт", "url1": "/question1_pg", "message2": "Далі"}
        session["user_id"] = user.id
        return jsonify(data), 200
    else:
        data = {"message": "Ви ще не зареестровані, або дані введені неправильно", "url1": "/", "message2": "Повернутися на головну сторінку"}
        return jsonify(data), 200

@app.route("/signUp_pg")
def f_3():
    return render_template("test_registration_sijax.html")

@app.route("/signUp", methods=["POST"])
def f_3_2():
    data = {"message": "Ви успішно зареєструвалися", "message2": "Далі"}
    name = request.form["name"]
    password = request.form["password"]
    mail = request.form["mail"]
    with Session() as session1:
        new_user = Users(name=name, email=mail, password=password)
        session1.add(new_user)
        session1.commit()
        session['user_id'] = new_user.id
    return jsonify(data), 200

@app.route("/question1_pg")
def f_4():
    return render_template("test_question1_sijax.html")

@app.route("/question1", methods=["POST"])
def f_4_2():
    data = {"message": "Далі"}
    answer = request.form['q1_info']
    user_answers_list.append(answer)
    global similarity
    if answer == "Суші":
        similarity += 1
    return jsonify(data), 200

@app.route("/question2_pg")
def f_5():
    return render_template("test_question2_sijax.html")

@app.route("/question2", methods=["POST"])
def f_5_2():
    data = {"message": "Далі"}
    answer = request.form['q2_info']
    user_answers_list.append(answer)
    global similarity
    if answer == "Мохіто":
        similarity += 1
    return jsonify(data), 200

@app.route("/question3_pg")
def f_6():
    return render_template("test_question3_sijax.html")

@app.route("/question3", methods=["POST"])
def f_6_2():
    data = {"message": "Далі"}
    answer = request.form['q3_info']
    user_answers_list.append(answer)
    global similarity
    if answer == "Болгарський перець, капуста Кольрабі, редиска":
        similarity += 1
    return jsonify(data), 200

@app.route("/question4_pg")
def f_7():
    return render_template("test_question4_sijax.html")

@app.route("/question4", methods=["POST"])
def f_7_2():
    data = {"message": "Далі"}
    answer = request.form['q4_info']
    user_answers_list.append(answer)
    global similarity
    if answer == "Яблуко, гранат, помело, мандаринки":
        similarity += 1
    return jsonify(data), 200

@app.route("/question5_pg")
def f_8():
    return render_template("test_question5_sijax.html")

@app.route("/question5", methods=["POST"])
def f_8_2():
    data = {"message": "Далі"}
    answer = request.form['q5_info']
    user_answers_list.append(answer)
    global similarity
    if answer == "Огірок, полуниця, кавун, виноград":
        similarity += 1
    return jsonify(data), 200

@app.route("/question6_pg")
def f_9():
    return render_template("test_question6_sijax.html")

@app.route("/question6", methods=["POST"])
def f_9_2():
    data = {"message": "Далі"}
    answer = request.form['q6_info']
    user_answers_list.append(answer)
    global similarity
    if answer == "Літо":
        similarity += 1
    return jsonify(data), 200

@app.route("/question7_pg")
def f_10():
    return render_template("test_question7_sijax.html")

@app.route("/question7", methods=["POST"])
def f_10_2():
    data = {"message": "Далі"}
    answer = request.form['q7_info']
    user_answers_list.append(answer)
    global similarity
    if answer == "Гроза зі зливою" or answer == "Швидкий товстий сніг" or answer == "Похмуро" or answer == "Легкий дощ":
        similarity += 1
    return jsonify(data), 200

@app.route("/question8_pg")
def f_11():
    return render_template("test_question8_sijax.html")

@app.route("/question8", methods=["POST"])
def f_11_2():
    data = {"message": "Далі"}
    answer = request.form['q8_info']
    user_answers_list.append(answer)
    global similarity
    if answer == "7":
        similarity += 1
    return jsonify(data), 200

@app.route("/question9_pg")
def f_12():
    return render_template("test_question9_sijax.html")

@app.route("/question9", methods=["POST"])
def f_12_2():
    data = {"message": "Далі"}
    answer = request.form['q9_info']
    user_answers_list.append(answer)
    global similarity
    if answer == "13":
        similarity += 1
    return jsonify(data), 200

@app.route("/question10_pg")
def f_13():
    return render_template("test_question10_sijax.html")

@app.route("/question10", methods=["POST"])
def f_13_2():
    data = {"message": "Далі"}
    answer = request.form['q10_info']
    user_answers_list.append(answer)
    global similarity
    if answer == "Математика" or answer == "Фізика" or answer == "Англійська мова" or answer == "Німецька мова" or answer == "Інша зарубіжна мова":
        similarity += 1
    return jsonify(data), 200

@app.route("/results_pg")
def f_14():
    return render_template("test_results_sijax.html")

@app.route("/results", methods=["POST"])
def f_14_2():
    with Session() as session1:
        user_id = session['user_id']
        if user_id:
            new_answers = Answers(user_id=user_id, answer1=user_answers_list[0], answer2=user_answers_list[1],
                                  answer3=user_answers_list[2], answer4=user_answers_list[3], answer5=user_answers_list[4],
                                  answer6=user_answers_list[5], answer7=user_answers_list[6], answer8=user_answers_list[7],
                                  answer9=user_answers_list[8], answer10=user_answers_list[9])
            session1.add(new_answers)
            session1.commit()
            final_similarity = f"{similarity * 10}%"
            data = {"message": final_similarity, "innerHTML1": '''`<p>Ви схожі на мене на ${response.message}</p>
            <a href="/">"Повернутися на головну сторінку"</a>
            <a href="/question1_pg>Пройти тест ще раз</a>
            <a href="/results_comparison_pg">Зрівняти відповіді</a>'''}
        else:
            data = {"innerHTML1": '`<p>"Ви ще не зареєстровані"</p>\n<a href="/">"Повернутися на головну сторінку"</a>'}
    return jsonify({"data": data}), 200

@app.route("/results_comparison_pg")
def f_15():
    return render_template("test_results_comparison_sijax.html")

@app.route("/results_comparison", methods=["POST"])
def f_15_2():
    with Session() as session1:
        user_id = session['user_id']
        if user_id:
            user_answers = session1.query(Answers).filter_by(user_id=user_id)
            data = [{"message1": i.answer1, "message2": i.answer2, "message3": i.answer3, "message4": i.answer4,
                     "message5": i.answer5, "message6": i.answer6, "message7": i.answer7, "message8": i.answer8,
                     "message9": i.answer9, "message10": i.answer10,
                     "innerHTML1": '''`<h5>1.Яка ваша улюблена їжа?</p>
            <p>Ваша відповідь: ${response.message1}</p>
            <p>Моя відповідь: суші</p>
            <h5>2.Який ваш улюблений напой?</p>
            <p>Ваша відповідь: ${response.message2}</p>
            <p>Моя відповідь: мохіто</p>
            <h5>3.Які ваші улюблені овочі?</p>
            <p>Ваша відповідь: ${response.message3}</p>
            <p>Моя відповідь: болгарський перець, капуста Кольрабі, редиска</p>
            <h5>4.Які ваші улюблені фрукти?</p>
            <p>Ваша відповідь: ${response.message4}</p>
            <p>Моя відповідь: яблуко, гранат, помело, мандаринки</p>
            <h5>5.Які ваші улюблені ягоди?</p>
            <p>Ваша відповідь: ${response.message5}</p>
            <p>Моя відповідь: огірок, полуниця, кавун, виноград</p>
            <h5>6.Яка ваша улюблена пора року?</p>
            <p>Ваша відповідь: ${response.message6}</p>
            <p>Моя відповідь: літо</p>
            <h5>7.Яка ваша улюблена погода?</p>
            <p>Ваша відповідь: ${response.message7}</p>
            <p>Моя відповідь: гроза зі зливою, швидкий товстий сні, похмуро, легкий дощ</p>
            <h5>8.Яка ваша улюблена цифра?</p>
            <p>Ваша відповідь: ${response.message8}</p>
            <p>Моя відповідь: 7</p>
            <h5>9.Яке ваше улюблене двузначне число?</p>
            <p>Ваша відповідь: ${response.message9}</p>
            <p>Моя відповідь: 13</p>
            <h5>10.Який ваш улюблений шкільний предмет?</p>
            <p>Ваша відповідь: ${response.message0}</p>
            <p>Моя відповідь: математика, фізика", англійська мова, німецька мова, інша зарубіжна мова</p>
            <a href="/">"Повернутися на головну сторінку"</a>
            <a href="/question1_pg>Пройти тест ще раз</a>'''} for i in user_answers]
        else:
            data = {"innerHTML1": '`<p>"Ви ще не зареєстровані"</p>\n<a href="/">"Повернутися на головну сторінку"</a>'}
    return jsonify({"data": data}), 200


if __name__ == "__main__":
    app.run(debug=True, port=8000)
