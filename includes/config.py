from libs.globals import Globals
from dotenv import load_dotenv
import os.path


class Config:

	# Constructor
	def __init__(self):
		filePath = Globals.getFullFilePath('/includes/configs/config.env')
		load_dotenv(filePath)


	# Read Config value
	def readConfigValue(self, variable):
		return False if (os.environ.get(variable) is None) else os.environ.get(variable)