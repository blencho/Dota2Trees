import unittest
import json
from mergeme import MyClass

class TestSteamQueries(unittest.TestCase):

	#def test_simple_request(self):
	       # Simple URL request to get server time and status
	#	url = ('http://api.steampowered.com/ISteamWebAPIUtil/GetServerInfo/'
	#		   'v0001/')
	#	data = steam_request(url, [])
	#	self.assertFalse(data is None)
		# print data

	def test_steam_key(self):
		# Get Latest Dota 2 Matches
		Jeff = MyClass()
		data = Jeff.get_recent_matches()
		self.assertFalse(data is None)
		print data
         






