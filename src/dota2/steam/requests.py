'''
Created on May 15, 2013

@author: Jeff
'''
import urllib2
import json
import zlib
import time
#from bs4 import BeautifulSoup
#import nltk

# Skill Levels
ANY_SKILL = 0
NORMAL_SKILL = 1
HIGH_SKILL = 2
VERY_HIGH_SKILL = 3

_STEAM_URL = "http://api.steampowered.com/"
_KEY = 'F7DB115339A12F8A0D76AF7250A5B1AD'
_HERO_NAME_PREFIX = 'npc_dota_hero_'

class SteamRequest(object):
    '''
    classdocs
    '''
    heroDict = {}
    requiredDict = {}
    specificationDict = {}
     
    def __init__(self):
        '''
        Constructor
        '''
        if not SteamRequest.heroDict:
            SteamRequest.heroDict = self._get_heroes() # TODO: not sure if thread safe
        
    # Thought this might simplify things. Can change whether or not it should send requests
    def steam_request(self, domain, cmd, params):
        url = _STEAM_URL
        url += domain + '/' + cmd + '/v1?key={0}'.format(_KEY) + '&format=json'
        for param in params:
            url += '&{0}'.format(param)
        try:
            data = urllib2.urlopen(url)
        except urllib2.URLError as err:
            print "URL Error {0}".format(err.reason)
            return None
        json_data = json.load(data)
        return json_data
        
    def _get_heroes(self):
        domain = 'IEconDOTA2_570'
        cmd = 'GetHeroes'
        tmpHeroDict = {}
        tmpJSON = self.steam_request(domain, cmd, [])
        heroList = tmpJSON['result']['heroes']
        for hero in heroList: 
            tmpHeroDict[str(hero['id'])] = hero['name'][len(_HERO_NAME_PREFIX):]
        return tmpHeroDict
    
    def setKey(self,key="4D7D7B6884092FAD9E59B6CAA572F588"):
        self.specificationDict['key'] = "key=%s" % key
        return
    
    def setPrimaryDomain(self,primaryDomain = "IDOTA2_570"):

        try:
            assert(primaryDomain in ["IDOTA2_570","IDOTA2Match_570","ISteamUser"])
        except AssertionError:
            print "Invalid primary domain. Defaulting to 'IDOTA2_570'"
            primaryDomain = "IDOTA2_570"
        
        self.requiredDict['primaryDomain'] = primaryDomain

    def get_hero(self, id):
        return SteamRequest.heroDict[str(id)]

    # Returns most recent, "Very High" skill games
    # Default matches returned is 25
    def get_recent_matches(self, nummatches=1, skill=NORMAL_SKILL, id=-1):
        domain = 'IDOTA2Match_570'
        cmd = 'GetMatchHistory'
        params = ['min_players=10', 'matches_requested={0}'.format(str(nummatches)), 
            'skill={0}'.format(str(skill))]
        if id != -1:
            params.extend(['account_id={0}'.format(str(id))])
        tmp_json = self.steam_request(domain, cmd, params)
        return tmp_json['result']
        
    """
    ======================================================================
    IDOTA2_570 Methods
    ======================================================================
    """
    
    
    """
    ======================================================================
    ISteamUser Methods
    ======================================================================
    """
    
    def getPlayerSummary(self, listOfPlayerIDS):
        pass
    

    # req = urllib2.Request("http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v1?format=json&appid=440&count=3&key=4D7D7B6884092FAD9E59B6CAA572F588&steamids=76561197970825781") # Create request object from URL
    # #req = urllib2.Request("http://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/v1?format=json&appid=440&count=3&key=4D7D7B6884092FAD9E59B6CAA572F588&display_name=penguinsmooches&date_min=1368580298&date_max=1368598684") # Create request object from URL
    # #print "."
    # opener = urllib2.build_opener() # Construct 'opener'
    # #print "."
    # jsonObj = opener.open(req) # Grab compressed file from URL with opener
    # #print "."
    # #decompressed = zlib.decompress(gzippedFile.read(), 16+zlib.MAX_WBITS) # Extract string version of JSON obj
    # tempJSON = json.load(jsonObj) # Convert string version of JSON obj to a JSON obj
    
    
        
jeff = SteamRequest()

#print jeff.tempJSON

'''
for match in jeff.tempJSON['result']['matches']:
    matchStr = ""
    for player in match['players']:
        print player
    print matchStr
'''

'''
for player in jeff.tempJSON['result']['matches'][1]['players']:
    print jeff.heroDict[str(player['hero_id'])]
'''
