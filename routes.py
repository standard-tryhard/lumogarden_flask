from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def grids():
	return render_template("grids.html")

@app.route("/trees")
def trees():
	return render_template("trees.html")

@app.route("/jars")
def jars():
	return render_template("jars.html")

@app.route("/cards")
def cards():
	return render_template("cards.html")

if __name__ ==  "__main__":
	app.run(debug=True)
