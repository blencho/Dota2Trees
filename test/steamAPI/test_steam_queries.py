import unittest
import json
from dota2.steam.requests import SteamRequest 

# class color:
#    PURPLE = '\033[95m'
#    CYAN = '\033[96m'
#    DARKCYAN = '\033[36m'
#    BLUE = '\033[94m'
#    GREEN = '\033[92m'
#    YELLOW = '\033[93m'
#    RED = '\033[91m'
#    BOLD = '\033[1m'
#    UNDERLINE = '\033[4m'
#    END = '\033[0m'

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
		data = Jeff.get_recent_matches()
		self.assertFalse(data is None)
		# print data

	def test_matches_by_player(self):
		# Get Latest Dota 2 Matches of the.Small.axe
		Jeff = SteamRequest()
		player_id = 76561198077179649
		data = Jeff.get_recent_matches(nummatches = 25, id=player_id)
		self.assertFalse(data is None)
		self.assertTrue(data['status'] == 1)
		for match in data['matches']:
			dire = []
			radiant = []
			player = []
			player_hero = ''
			for player in match['players']:
				hero = SteamRequest.heroDict[str(player['hero_id'])]
				if (int(player['account_id']) + 76561197960265728) == player_id: # convert 32-bit to 64-bit steam id
					player_hero = hero
				if player['player_slot'] >> 7 & 0x1:
					radiant.extend([hero])
				else:
					dire.extend([hero])
			header = '{0} {1:^5} {2}'.format('Radiant'.ljust(16), '', 'Dire'.ljust(16))
			print '\n' + header
			print '-' * len(header)
			print 'Player:\t\033[91m{0}\033[0m'.format(player_hero) # prints player hero in red
			for i, (radPlayer, direPlayer) in enumerate(zip(radiant, dire)):
				vs = False
				if i == 2:
					vs = True
				print '{0} {1:^5} {2}'.format(radPlayer.ljust(16), 
					'vs' if vs else '', direPlayer.ljust(16))
