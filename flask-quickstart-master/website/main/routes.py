from flask import render_template, Blueprint
main = Blueprint('main', __name__)

@main.route("/", methods=['GET'])
def home():
	return render_template("index.html")


