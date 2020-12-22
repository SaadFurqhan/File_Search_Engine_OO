from src.SearchEngine import app
from flask import Flask, render_template, request

@app.errorhandler(404)
def error1(e):
    return render_template("404.html")

@app.errorhandler(500)
def error2(e):
    return render_template("500.html")

@app.errorhandler(403)
def error3(e):
    return render_template("403.html")

