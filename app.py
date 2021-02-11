from flask import Flask,render_template,url_for,request,request
from psql_functions import *


torus = Flask(__name__)


@torus.route("/",methods=['GET', 'POST'] )
def torusa():
    return  render_template('index.html')


@torus.route('/add_contacts', methods=["POST", "GET"])
def add_contacts():
    if request.method == "GET":
        return render_template("add_contacts.html")
    else:
        name = request.form["name"]
        companyid = request.form["company"]

        insertion = {
            "full_name" : name,
            "companyid" : companyid
        }

        Insert(insertion)

        return redirect("/")


@torus.route("/all_contacts",methods=['GET', 'POST'] )
def function():
    if request.method == "GET":
        contacts = []
        _all = []            
        rows = Select_All()
        for row in rows:
            each = {
                "_id" : row[0],
                "full_name" : row[1],
                "companyid" : row[2]
            }
            _all.append(each)
        for each in _all:
            if each["full_name"] != "":
                insertion = {
                    "id" : str(each["_id"]),
                    "full_name" : each["full_name"],
                    "companyid" : each["companyid"]
                }
                contacts.append(insertion)
        return render_template("all_contacts.html", contacts=contacts)

@torus.route('/contacts_modification', methods=["POST", 'GET'])
def contacts_modification():
    if request.method == "GET":
        _id = request.args.get("id")
        name = request.args.get("full_name")
        comp = request.args.get("company")
        
        # GET DATA FROM PSQL
        row = Select_One(_id)
        data = {
            "id" : row[0],
            "full_name" : row[1],
            "companyid" : row[2]
        }

        print(data)
        return render_template('contacts_modification.html', data=data)
    else:
        fullname = request.form["full_name"]
        _id = request.args.get("id")

        Update(_id, full_name)

        return redirect("/")

@torus.route('/delete_contacts', methods=["POST", 'GET'])
def delete_contact():
    if request.method == "GET":
        _id = request.args.get("id")
        _route = request.args.get("route")
        Delete_One(_id)
        
        if _route == "deleted":
            return redirect("/contacts_modification")
        else:    
            return redirect("/")


if __name__ == '__main__':
    torus.run(host="0.0.0.0", port=8080, debug=True)
