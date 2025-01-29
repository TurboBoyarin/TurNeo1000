from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/user/<string:name>/<int:id>')
def user(name, id):
    return "User: " + name + " - " + str(id)


if __name__ == "__main__":
    app.run(debug=True)

