import unittest
import json
from dota2.steam.steamrequests import SteamRequest 

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
		Jeff = SteamRequest()
		data = Jeff.get_recent_matches(['matches_requested=1'])
		self.assertFalse(data is None)
		# print data

	def test_matches_by_player(self):
		# Get Latest Dota 2 Matches of the.Small.axe
		Jeff = SteamRequest()
		data = Jeff.get_recent_matches(['account_id=76561198077179649',])
		self.assertFalse(data is None)
		self.assertTrue(data['status'] == 1)
		for match in data['matches']:
			dire = []
			radiant = []
			for player in match['players']:
				hero = Jeff.heroDict[str(player['hero_id'])]
				if player['player_slot'] >> 7 & 0x1:
					radiant.extend([hero])
				else:
					dire.extend([hero])
			header = '{0} {1:^5} {2}'.format('Radiant'.ljust(16), '', 'Dire'.ljust(16))
			print header
			print '-' * len(header)
			for i, (radPlayer, direPlayer) in enumerate(zip(radiant, dire)):
				vs = False
				if i == 2:
					vs = True
				print '{0} {1:^5} {2}'.format(radPlayer.ljust(16), 
					'vs' if vs else '', direPlayer.ljust(16))