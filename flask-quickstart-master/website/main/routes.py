#from testing import ts
from flask import render_template, Blueprint
main = Blueprint('main', __name__)

@main.route("/", methods=['GET'])
def home():
	return render_template("index.html")


"""
from flask import render_template, Blueprint
import testing
main = Blueprint('main', __name__)

@main.route("/", methods=['GET'])
def home():
	return render_template("index.html")
    
@main.route("/dog", methods=["GET"])
def dog():
    return render_template("dog.html")

depart_course = testing.read_csv("courses/COM")
departments = depart_course[0]
courses = depart_course[1]

##apply prereqs
for e in courses():
    definePrereqs(departments,e[0],e[1])

c = lookUpCourse(departments,courses[0][0],courses[0][1])
print(c.name)

input = "??"
courses = []

@main.route("/testing")
def testing():
    return render_template("testing.html",courses)

"""
#depart_course = ts.read_csv("courses/COM")
#departments = depart_course[0]
#courses = depart_course[1]

##apply prereqs
#for e in courses():
#    definePrereqs(departments,e[0],e[1])

#c = lookUpCourse(departments,courses[0][0],courses[0][1])
#print(c.name)

#input = "??"
#courses = []

#@main.route("/testing")
#def testing():
#    return render_template("testing.html",courses)
