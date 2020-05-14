from flask import Flask, render_template,redirect, request
import joblib

app = Flask(__name__)

model= joblib.load("model.pkl")

friends= ["Prateek","Jatin","Sohail"]

num=5


@app.route("/")
def hello():
	return render_template("index.html")

@app.route('/',methods=['POST'])
def marks():
	if request.method== 'POST':
		hours= float(request.form['hours'])

		marks= str(model.predict([[hours]]))

	return render_template("index.html", your_marks= marks)


if __name__ == '__main__':
	app.run(debug=True)