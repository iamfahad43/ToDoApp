# codes

from crypt import methods
from flask import Flask, request, jsonify

app = Flask(__name__)

# the route point
@app.route('/', methods=['GET', 'POST'])
def route():
    return jsonify({"Greetings": "Welcome to Python Assignment given by Integrify",
                    "Author": "Fahad Mahmood"})

# sign up
@app.route('/api/v1/signup/', methods=["POST"])
def singup():
    UserEmail = request.form['email']
    UserPass = request.form['password']
    return jsonify("successfully called signup endpoint")       
    
# sign in
@app.route('/api/v1/signin/', methods=["POST"])
def singin():
    UserEmail = request.form['email']
    UserPass = request.form['password']
    return jsonify("successfully called signin endpoint")  

# changePassword
@app.route('/api/v1/changePassword/', methods=["PUT"])
def changePassword():
    oldPass = request.form['old-password']
    newPass = request.form['new-password']
    return jsonify("successfully called changePassword endpoint")   
  
# todo list
@app.route('/api/v1/todos?status=[status]/', methods=["GET"])
def todo_list():
    oldPass = request.form['old-password']
    newPass = request.form['new-password']
    return jsonify("successfully called todo list endpoint")   
  
# todos
@app.route('/api/v1/todos/', methods=["POST"])
def todos():
    oldPass = request.form['old-password']
    newPass = request.form['new-password']
    return jsonify("successfully called todos endpoint")   
  
# update todo list
@app.route('/api/v1/todos/:id/', methods=["PUT"])
def update_todo():
    oldPass = request.form['old-password']
    newPass = request.form['new-password']
    return jsonify("successfully called update todo list endpoint") 

# delete todo list
@app.route('/api/v1/todos/:id/', methods=["DELETE"])
def delete_todo():
    oldPass = request.form['old-password']
    newPass = request.form['new-password']
    return jsonify("successfully called delete todo list endpoint")
    
if __name__=="__main__":
    app.run(debug=True)
