from flask import Flask, render_template, request, redirect

# * Creating an WSGI = web server gateway interface application
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", title="Home Page")


@app.route("/about")
def about():
    return render_template("index.html", title="About Page")


# showing html form to the user
@app.route("/register", methods=["GET"])
def register_form():
    return render_template("register.html")


# showing html form to the user
@app.route("/register", methods=["POST"])
def handle_register():
    name = request.form.get("name")
    email = request.form.get("email")
    password = request.form.get("password")
    if password != "secret":
        return redirect("/register")
    return render_template("welcome.html", user=name, type="admin")


if __name__ == "__main__":
    app.run(debug=True, port=8000)
