import json
import urllib2

KEY = 'F7DB115339A12F8A0D76AF7250A5B1AD'

def steam_request(url, params):
	if url[-1] != '/':
		url += '/'
	url += '?key={0}'.format(KEY)
	for param in params:
		url += '&{0}'.format(param)
	try:
		data = urllib2.urlopen(url)
	except urllib2.URLError as err:
		print "URL Error {0}".format(err.reason)
		return None
	json_data = json.load(data)
	return json_data

def update_heroe_list():
	url = 'http://api.steampowered.com/IEconDOTA2_570/GetHeroes/v1/'
	heroes = steam_request(url, None)
	# heroes: list 
	# 	name
	# 	id
	# 	localized_name (used in name display)
	# count


