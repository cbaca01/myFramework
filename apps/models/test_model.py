from libs.globals import Globals
from includes.table_mapper import TableMapper

class TestModel(object):

	__db = None
	__books = None
	__property_types = None

	session = None


	#Constructor
	def __init__(self, db):
		self.__db = db

		# Get session
		self.session = self.__db.session

		# Get tables needed
		self.__books = TableMapper(self.__db.table.books, self.session)
		self.__property_types = TableMapper(db.table.property_types, self.session)


	# Retrieve results
	def getResults(self):
		return self.__db.fetchAll(self.__books.select())


	# Store data
	def store(self, data):
		return self.__books.insert(data)


	# Update data
	def update(self, data, params, **kwargs):
		return self.__db.fetchAll(self.__books.update(data, params))


	# Delete data
	def delete(self, params):
		return self.__db.fetchAll(self.__books.delete(params))


	# Raw Query
	def getBooksRAW(self, params=None):
		query = 'SELECT * FROM books WHERE id = :id ORDER BY title'
		return self.__db.fetchRow(self.__db.genRAWCall(query, params=params))


	# Stored Procedure
	def getPropertyByID(self, params=None):
		return self.__db.fetchRow(self.__db.genStoredProcedureCall('test_schema.getallpropertytypestableset', params=params))