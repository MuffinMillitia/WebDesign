from flask import Flask, render_template, request

app = Flask(__name__)

projects = ["project1", "project2", "project3", "project4"]


@app.route("/")
def index():
    return render_template("index.html", projects=projects)


@app.route("/<which_project>/")
def project_page(which_project):
    return render_template("{}.html".format(which_project))