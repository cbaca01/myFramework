# This class contains our helper functions
# NOTE: all class methods must be static
import os.path
import sys, json, string, random, socket, logging
import numpy as np

class Globals:
	# Parse JSON File and return tuple
	@staticmethod
	def getFullFilePath(filePath):
		# stripping include from file path
		filePath = (os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))).strip('include') + filePath
		filePath = filePath.replace('//', '/')

		return filePath


	@staticmethod
	def parseJSONFile(filePath):
		# getting full filepath
		filePath = Globals.getFullFilePath(filePath)

		# opening file path
		data  = []
		with open(filePath) as data_file:
			data = json.load(data_file)

		return (data if len(data)>0 else False)


	# Get number of dimensions
	@staticmethod
	def checkIfMultiDimensional(array):
		array = list(array)
		return isinstance(array[0], dict)


	# Display in error_log
	@staticmethod
	def writeToErrorLog(str):
		return True