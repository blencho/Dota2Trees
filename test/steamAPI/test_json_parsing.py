import unittest
import json

from requesthelper import steam_request

class TestJSONParsing(unittest.TestCase):

	def setUp(self):
		url = ('http://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/v1/')
		params = ['matches_requested=1']
		data = steam_request(url, params)

	def test_

