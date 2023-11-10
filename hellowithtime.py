from flask import Flask
from pytz import timezone
from datetime import datetime
import pendulum

app = Flask(__name__)

@app.route("/")
def hello():
	return "Hello World!"

	Ind = pendulum.timezone('Asia/Kolkata')

	print("Current Time in India: ", datetime.now(Ind))



if __name__ == "__main__":
	app.run(debug=True)