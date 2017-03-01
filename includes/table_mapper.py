from libs.globals import Globals

class TableMapper(object):

	__table = None
	__session = None

	# Constructor
	def __init__(self, table, session):
		self.__table = table
		self.__session = session


	# Get All Records
	def select(self, params=None):
		if params is None:
			return self.__session.query(self.__table).all()
		else:
			return self.__session.query(self.__table).filter_by(**params)


	# Insert Record
	def insert(self, data):
		# Check if object is multidimensional
		# If TRUE then iterate through array and statements to session
		if Globals.checkIfMultiDimensional(data) == True:
			lastInsertID = []
			for row in data:
				query = self.__table(**row)
				self.__session.add(query)
				self.__session.flush()
				lastInsertID.append(query.id)
		else:
			query = self.__table(**data)
			self.__session.add(query)
			self.__session.flush()
			lastInsertID = query.id

		return lastInsertID


	# Update Record
	def update(self, data, params, **kwargs):
		query = self.__session.query(self.__table).filter_by(**params).update(data)
		self.__session.flush()
		return self.select(params)


	# Delete Record
	def delete(self, params, **kwargs):
		query = self.__session.query(self.__table).filter_by(**params).delete()
		self.__session.flush()
		return self.select(params)