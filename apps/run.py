from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def index():
	return jsonify({'id': 22})

# import our controller and register
from apps.controllers.test_controller import TestController as tc
tc.register(app)


if __name__ == '__main__':
	# app.run(debug=True)
	app.debug = True