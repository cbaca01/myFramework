from libs.globals import Globals
from includes.config import Config

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine, text
from sqlalchemy.sql import select

class Database:
	__host = None
	__username = None
	__password = None
	__database = None

	__engine = None
	__connection = None
	__dataObject = {}

	table = None
	session = None

	#Constructor
	def __init__(self):
		global Config
		Config = Config()

		self.__host = Config.readConfigValue('DB_HOST')
		self.__username = Config.readConfigValue('DB_USERNAME')
		self.__password = Config.readConfigValue('DB_PASSWORD')
		self.__database = Config.readConfigValue('DB_NAME')


	# Making connection
	def connect(self):
		# Making connection
		self.__engine = create_engine('postgresql://' + self.__username + ':' + self.__password + '@' + self.__host + '/' + self.__database, convert_unicode=True, echo=False)
		self.__connection = self.__engine.connect()

		# Creating session
		self.session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=self.__engine))

		# reflecting the tables
		Base = automap_base()
		Base.prepare(self.__engine, reflect=True)
		self.table = Base.classes	
		

	# Get Results
	def __getResults(self, dataObject):
		for row in dataObject:
			self.__dataObject[len(self.__dataObject)] = self.__convertRowToDict(row)


	# IF data list has more than 1 item then return multi-list
	def fetchAll(self, dataObject):
		self.__getResults(dataObject)
		return self.__dataObject


	# IF data list has 1 item dataObject then return first index
	def fetchRow(self, dataObject):
		self.__getResults(dataObject)
		return self.__dataObject[0]


	# Create stored procedure call
	def genStoredProcedureCall(self, proc, params=None, **kwargs):
		# creating db function parameters if they exist
		if params != None and len(params) > 0:
			paramsCall = '('
			for key in params:
				paramsCall+= 'i_' + key + ' := :' + key
			paramsCall+= ')'

			results = self.__connection.execute(text('SELECT * FROM ' + proc + paramsCall), params, **kwargs)
		else:
			results = self.__connection.execute(text('SELECT * FROM ' + proc + '()'))
		return results


	# Create RAW SQL call
	def genRAWCall(self, query, params=None, data=None, **kwargs):
		if params==None:
			results = self.__connection.execute(text(query))
		else:
			results = self.__connection.execute(text(query), params, **kwargs)
		return results


	# Make row mapper
	def __convertRowToDict(self, row):
		if hasattr(row, 'items'):
			return {str(c[0]): row[c] for c in row.items()}
		else:
			return {str(c.name): getattr(row, c.name) for c in row.__table__.columns}


	# Close Connection
	def closeConnection(self):
		self.session.close()
		self.__connection.close()