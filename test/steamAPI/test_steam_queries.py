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

	def test_recent_matches(self):
		# Get Latest Dota 2 Matches
		Jeff = MyClass()
		data = Jeff.get_recent_matches(['matches_requested=1'])
		self.assertFalse(data is None)
		#print data

	def test_matches_by_player(self):
                # Get Latest Dota 2 Matches of the.Small.axe
                Jeff = MyClass()
                data = Jeff.get_recent_matches(['account_id=76561198077179649',])
                
                self.assertFalse(data is None)
                print data
         






