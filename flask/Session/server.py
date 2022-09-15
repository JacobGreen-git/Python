from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "Is it secret? Is it safe?"

@app.route('/')
def index():
    if "count" not in session:
        session["count"] = 1
    return render_template("index.html")    

@app.route("/plus1", methods=["POST"])
def view_count():
    session["count"] += 1
    return redirect("/")

@app.route("/reset")
def reset():
    session.clear()
    return redirect("/")

if __name__=="__main__":  
    app.run(debug=True) 