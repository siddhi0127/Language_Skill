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
if __name__ == "__main__":
    app.run(debug=True)

