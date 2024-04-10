from datetime import datetime
from flask import request, Flask, render_template, url_for, redirect, session
from sqlalchemy import Column, create_engine, String, ForeignKey, Date
from sqlalchemy.orm import DeclarativeBase, sessionmaker, Mapped, mapped_column
from flask import request, Flask, render_template, url_for, redirect, session, jsonify

app = Flask(__name__)
app.config['SECRET_KEY'] = '12212112'
app.config["PERMANENT_SESSION_LIFETIME"]

engine = create_engine("sqlite:///sijax_registration_db.db", echo=True)
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
    password: Mapped[str] = mapped_column(String(80))

class Favourite_food(Base):
    __tablename__ = "favourite_food"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    favourite_food: Mapped[str] = mapped_column(String(80))

# base = Base()
# base.create_db()

@app.route("/")
def f_1():
    return render_template("sijax_registration_pg1.html")

@app.route("/login_pg")
def f_2():
    return render_template("sijax_registration_pg2.html")

@app.route("/login", methods=["POST"])
def f_2_2():
    name = request.form["name"]
    password = request.form["password"]
    with Session() as session1:
        user = session1.query(Users).filter_by(name=name, password=password).first()
    if user:
        data = {"message": "Ви успішно війшли в аккаунт", "url1": "/favourite_food_pg", "message2": "Далі"}
        session["user_id"] = user.id
        return jsonify(data), 200
    else:
        data = {"message": "Ви ще не зареестровані, або дані введені неправильно", "url1": "/", "message2": "Повернутися на головну сторінку"}
        return jsonify(data), 200

@app.route("/signUp_pg")
def f_3():
    return render_template("sijax_registration_pg3.html")

@app.route("/signUp", methods=["POST"])
def f_3_2():
    data = {"message": "Ви успішно зареєструвалися", "message2": "Далі"}
    name = request.form["name"]
    password = request.form["password"]
    with Session() as session1:
        new_user = Users(name=name, password=password)
        session1.add(new_user)
        session1.commit()
        session["user_id"] = new_user.id
    return jsonify(data), 200

@app.route("/favourite_food_pg")
def f_4():
    return render_template("sijax_registration_pg4.html")

@app.route("/favourite_food", methods=["POST"])
def f_4_2():
    food = request.form["info1"]
    with Session() as session1:
        user_id = session["user_id"]
        if user_id:
            new_info = Favourite_food(user_id=user_id, favourite_food=food)
            session1.add(new_info)
            session1.commit()
            data = {"innerHTML1": '`<p>"Інформація успішно зережена"</p>\n<a href="/favourite_food_pg">"Записати ще улюблені страви"</a>\n<a href="/check_favourite_food_pg">"Продивитися усі записані вами ваші улюблені страви"</a>`'}
        else:
            data = {"innerHTML1": '`<p>"Ви ще не зареєстровані"</p>\n<a href="/">"Повернутися на головну сторінку"</a>'}
    return jsonify(data), 200

@app.route("/check_favourite_food_pg")
def f_5():
    return render_template("sijax_registration_pg5.html")

@app.route("/check_favourite_food", methods=["POST"])
def f_5_2():
    with Session() as session1:
        user_id = session["user_id"]
        if user_id:
            all_food = session1.query(Favourite_food).filter_by(user_id=user_id)
            data = [{"message": i.favourite_food} for i in all_food]
        else:
            data = {"message": "Ви ще не записували ваші улюблені страви"}
    return jsonify({"data": data}), 200

if __name__ == "__main__":
    app.run(debug=True, port=8000)
