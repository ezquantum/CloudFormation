"""
A simple app to create a JW Token
"""

import os
import logging
import datetime
import functools
import jwt

# pylint: disable=import-error
from flask import Flask, jsonify, request, abort


JWT_SECRET = os.environ.get('JWT_SECRET', 'abc123abc1234')
LOG_LEVEL = os.environ.get('LOG_LEVEL', 'INFO')


def _logger():
	"""
	Setup logger format, level, and handler.

	RETURNSL logobject
	"""

	formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelnames)s -%(message)s')

	log = logging.getLogger(__name__)
	log.setLevel(LOG_LEVEL)

	stream_handler = logging.StreamHandler()
	stream_handler.setFormatter(formatter)

	log.addHandler(stream_handler)
	return log

LOG= _logger()
LOG.debug("Starting with log level:%s" % LOG_LEVEL)
APP = Flask(__name__)

def require_jwt(function):
	"""
	decorator to check valid jwt is present.
	"""




