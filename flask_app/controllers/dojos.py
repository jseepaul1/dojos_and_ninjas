from flask_app import app
from flask import render_template, redirect, request, session

from flask_app.models.dojo import Dojo


@app.route("/")
def index():
    return redirect("/dojos")

@app.route("/dojos")
def dojos():
    return render_template("display_dojo.html", dojos=Dojo.get_all())


@app.route("/dojo/create", methods=["POST"])
def create_dojo():
    Dojo.save(request.form)
    return redirect("/dojos")

@app.route('/dojo/<int:id>')
def show_dojo(id):
    data = {
        "id": id
    }
    return render_template('ninjas_with_dojo.html', dojo=Dojo.get_one(data))