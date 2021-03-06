from flask import Flask, render_template, request, jsonify
from flask.ext.classy import FlaskView, route

from libs.globals import Globals
from includes.database import Database

from apps.models.test_model import TestModel

class TestController(FlaskView):
	route_base = '/books/'

	__db = Database()
	__testModel = None

	def __init__(self):
		app = Flask(__name__)

		self.__db.connect()
		self.__testModel = TestModel(self.__db)


	# Index
	@route('/')
	def index(self):
		return jsonify({'string': 'hi!'})


	# custom route
	@route('/getall', strict_slashes=False)
	def getAll(self):
		results = self.__testModel.getResults()
		return jsonify(results)


	# custom route
	@route('/book_id/<int:bookID>', strict_slashes=False)
	def getBookID(self, bookID):
		params = {'id': bookID}
		results = self.__testModel.getBooksRAW(params)
		return jsonify(results)


	# Destructor
	def __del__(self):
		self.__db.closeConnection()