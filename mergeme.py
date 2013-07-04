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

class MyClass(object):
    '''
    classdocs
    '''
    url = ""
    heroDict = {}
    requiredDict = {}
    specificationDict = {}

    def __init__(self):
        '''
        Constructor
        '''
        url = "http://api.steampowered.com/ISteamNews/GetNewsForApp/v0001/?format=json&appid=440&count=3"
        self.heroDict = self.getHeroes()
        
    def getHeroes(self):
        req = urllib2.Request("http://api.steampowered.com/IEconDOTA2_570/GetHeroes/v1?format=json&appid=440&count=3&key=4D7D7B6884092FAD9E59B6CAA572F588&display_name=penguinsmooches&skill=3") # Create request object from URL
        opener = urllib2.build_opener() # Construct 'opener'
        jsonObj = opener.open(req) # Grab compressed file from URL with opener
        tempJSON = json.load(jsonObj) # Convert string version of JSON obj to a JSON obj
        heroList = tempJSON['result']['heroes']
        for hero in heroList: 
            self.heroDict[str(hero['id'])] = hero['name']
        return
    
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
    

    req = urllib2.Request("http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v1?format=json&appid=440&count=3&key=4D7D7B6884092FAD9E59B6CAA572F588&steamids=76561197970825781") # Create request object from URL
    #req = urllib2.Request("http://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/v1?format=json&appid=440&count=3&key=4D7D7B6884092FAD9E59B6CAA572F588&display_name=penguinsmooches&date_min=1368580298&date_max=1368598684") # Create request object from URL
    #print "."
    opener = urllib2.build_opener() # Construct 'opener'
    #print "."
    jsonObj = opener.open(req) # Grab compressed file from URL with opener
    #print "."
    #decompressed = zlib.decompress(gzippedFile.read(), 16+zlib.MAX_WBITS) # Extract string version of JSON obj
    tempJSON = json.load(jsonObj) # Convert string version of JSON obj to a JSON obj
    
    
        
jeff = MyClass()

print jeff.tempJSON

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
