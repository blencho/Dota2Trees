import os
import re
import StringIO
import json

RESOURCE_DIR = os.path.join(os.path.dirname(__file__), os.pardir, 'resources')
HERO_FILE = RESOURCE_DIR + '/npc_heroes.txt'
ABILITY_FILE = RESOURCE_DIR + '/npc_abilities.txt'

VDF_LINE_FORMAT = r"\"(\w+)\"\s+\"(\w+)\""


def update():
	_load_heroes()
	# _load_abilities()
#
# ==================================================================================
#
def _load_heroes():
	#
	fh 				= open(HERO_FILE)
	heroes 			= {}
	stack 			= []
	curHeroBlock	= ""
	beginNewBlock	= False
	bracketDepth	= 0
	#
	openToken	= re.compile("{")
	clsdToken	= re.compile("}")
	heroToken	= re.compile(r"\bnpc_dota_hero_(\w+)")
	#
	for line in fh:
		#
		if beginNewBlock:
			#
			opened	= openToken.search(line)
			#
			if opened is not None:
				#
				bracketDepth += 1
				#
			else:
				#
				closed	= clsdToken.search(line)
				#
				if closed is not None:
					#
					bracketDepth -= 1
					#
				#
			#
			if (bracketDepth > 0):
				#
				curHeroBlock += line
				#
			else:
				#		
				setHeroDictionary(hero, curHeroBlock)
				heroes[hero['Name']] = hero
				beginNewBlock 	= False
				curHeroBlock	= ""
			#
		else:
			#
			m	= heroToken.search(line)
			#
			if (m is not None):
				#
				hero 			= {}
				hero['Name'] 	= m.group(1)
				beginNewBlock	= True
				#
			#
		#
	#
	with open('heroes.json', 'w') as outFile:
		json.dump(heroes, outFile, sort_keys = True, indent = 4)
	#
	return

def setHeroDictionary(heroDict, heroBlock):
	#
	tokenList	= [	"General", "Abilities", "Armor", "Attack", "Attributes", "Bounty", 
					"Bounds", "Movement", "Status", "Team", "Vision"]
	#
	for token in tokenList:
		heroDict[token]	= parseItem(heroBlock, token)
	#
	return

def parseItem(heroBlock, itemName):
	beginItemBlock 	= False
	endItemBlock	= False
	lineList		= heroBlock.splitlines()
	itemDictionary	= {}
	#
	itemToken		= re.compile("// " + itemName)
	subItemToken	= re.compile('\"(.+)\"\s+\"(.+)\"')
	nextItemToken	= re.compile("// \w+")
	#
	for line in lineList:
		#
		itemMatch	= itemToken.search(line)
		#
		if beginItemBlock:
			#
			if endItemBlock:
				#
				return itemDictionary
				#
			else:
				#
				subItemMatch	= subItemToken.search(line)
				#
				if subItemMatch is not None:
					#
					itemDictionary[subItemMatch.group(1)]	= subItemMatch.group(2)
					#
				else:
					#
					nextItemMatch = nextItemToken.search(line)
					#
					if nextItemMatch is not None:
						#
						endItemBlock = True
						#
					#
				#
			#
		elif itemMatch is not None:
			#
			beginItemBlock = True
			#
		#
	#
	return itemDictionary

#
# ==================================================================================
#
#def _parse_hero_node(fh, node):
#		scanner = re.Scanner([
#		(r"\"\w+\"\s+\"\w+\"\.*", _parse_tuple),
#		(r"{", ),
#		(r"//\.+". None),
#
#	])
#
# ==================================================================================
#
class hero():
	#
	#
	#
	def __init(self):
		return
#
#
#

	