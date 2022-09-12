#server.py NEEDS TO IMPORT flask_app folder and whatever controllers you are using.
from flask_app import app
from flask_app.controllers import users_controller

if __name__=="__main__":
    app.run(debug=True)