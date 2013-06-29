import unittest
import json

from requesthelper import steam_request

class TestSteamQueries(unittest.TestCase):

	def test_simple_request(self):
		# Simple URL request to get server time and status
		url = ('http://api.steampowered.com/ISteamWebAPIUtil/GetServerInfo/'
			   'v0001/')
		data = steam_request(url, [])
		self.assertFalse(data is None)
		# print data

	def test_steam_key(self):
		# Get Latest Dota 2 Match
		url = ('http://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/v1/')
		params = ['matches_requested=1']
		data = steam_request(url, params)
		self.assertFalse(data is None)
		# print data






