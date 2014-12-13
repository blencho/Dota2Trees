from requests import SteamRequest

class DotaPlayer(object):

	def __init__(self, json_string):
		steam = SteamRequest()
		self.account_id = int(json_string['account_id'])
		self.slot = int(json_string['player_slot'])
		self.hero = steam.getHero(json_string['hero_id']
		self.level = json_string['level']
		self.items = [json_string['item_0'], json_string['item_1'],
			json_string['item_2'], json_string['item_3'], 
			json_string['item_4'], json_string['item_5']]
		self.kills = json_string['kills']
		self.deaths = json_string['deaths']
		self.assists = json_string['assists']
		self.cs = json_string['last_hits']
		self.denies = json_string['denies']
		self.gpm = json_string['gold_per_min']
		self.xppm = json_string['xp_per_min']
		for summon in json_string['additional_units']:
			print summon['unitname']
			# TODO: handle syllabear items

class DotaMatch(object):

	def __init__(self, json_string):
		self.radiant = []
		self.dire = []
		for json_player in json_string['players']:
			player = DotaPlayer(json_player)
			tmpDict = None
			if (player.slot & 0x80) == 0: # Check 8th bit
				tmpDict = self.radiant
			else:
				tmpDict = self.dire
			tmpDict.insert([player, (player.slot & 0x7)])
		if json_string['radiant_win'] == '1':
			self.winner = 'radiant' # TODO: string or enum/define?
		else:
			self.winner = 'dire'
		# Game type
		# 0 - Public matchmaking
		# 1 - Practice
		# 2 - Tournament
		# 3 - Tutorial
		# 4 - Co-op with bots.
		# 5 - Team match
		# 6 - Solo Queue
		self.type = int(json_string['lobby_type'])
