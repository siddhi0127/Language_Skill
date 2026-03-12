# import os
# print(os.path.exists("users.db"))

import sqlite3

from flask import Flask, render_template, request, redirect, session
import os
app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY")

@app.route("/")
def login_page():
    return render_template("login.html")

@app.route("/login",methods=["POST"])
def login():
    name=request.form["name"]
    password=request.form["password"]
    
    conn= sqlite3.connect("users.db")
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM tblregister WHERE name= ? AND password =?",(name,password))

    user=cursor.fetchone()
    conn.close()

    if user:
        return redirect("/dashboard")
    else:
        return "Invalid Email or password"

@app.route("/register",methods=["GET","POST"])
def register():
    if request.method == "POST":
        name=request.form["name"]
        email=request.form["email"]
        password=request.form["password"]
        

        conn=sqlite3.connect("users.db")
        cursor=conn.cursor()

        cursor.execute("INSERT INTO tblregister(name,email,password) VALUES(?,?,?)",(name,email,password))
        conn.commit()
        conn.close()

        return redirect("/")
    return render_template("register.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/quiz", methods=["GET","POST"])
def quiz():
    if request.method == "POST":
        domain=request.form.get("domain")
        conn=sqlite3.connect('users.db')
        cursor=conn.cursor()
        
        cursor.execute("SELECT * FROM tblquestion WHERE domain=? LIMIT 10",(domain,) )
        questions=cursor.fetchall()
        conn.close()
        
        return render_template("quiz.html",questions=questions)
    
@app.route("/submit_test",methods=["POST"])
def submit_test():
    conn=sqlite3.connect("users.db")
    cursor=conn.cursor()
    
    cursor.execute("SELECT id,answer FROM tblquestion")
    questions = cursor.fetchall()
    
    for key in request.form:
        if key.startswith("q"):
            qid = key[1:]   
            user_answer = request.form.get(key)

            cursor.execute(
                "SELECT answer FROM tblquestion WHERE id=?",
                (qid,)
            )

            correct_answer = cursor.fetchone()[0]

            if user_answer == correct_answer:
                score += 1

    conn.close()
    return render_template("result.html", score=score)

if __name__ == "__main__":
    app.run(debug=True)

