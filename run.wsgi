#!/usr/bin/python

import sys, logging, os

path = os.path.dirname(__file__)
if path not in sys.path:
	sys.path.insert(0, path)

from includes.config import *
Config = Config()

logging.basicConfig(stream=sys.stderr)

sys.path.insert(0, Config.readConfigValue('PROJECT_ROOT'))

from apps.run import app as application