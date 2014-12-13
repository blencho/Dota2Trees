import os
import re

RESOURCE_DIR = os.path.join(os.path.dirname(__file__), os.pardir, 'resources')
HERO_FILE = RESOURCE_DIR + '/npc_heroes.txt'
ABILITY_FILE = RESOURCE_DIR + '/npc_abilities.txt'

VDF_LINE_FORMAT = r"\"(\w+)\"\s+\"(\w+)\""


def update():
	_load_heroes()
	# _load_abilities()


def _load_heroes():
	fh = open(HERO_FILE)
	heroes = []
	stack = []
	for line in fh:
		p = re.compile(r"\bnpc_dota_hero_(\w+)")
		m = p.match(line)
		if (m.group(0) is None):
			continue
		hero = {}
		hero['name'] = m.group(0)
		if _parse_hero_node(fh, hero) == -1:
			return -1
		heroes.apend(hero)


def _parse_hero_node(fh, node):
		scanner = re.Scanner([
		(r"\"\w+\"\s+\"\w+\"\.+", _parse_tuple),
		(r"{", ),
		(r"//\.+". None),

	])
