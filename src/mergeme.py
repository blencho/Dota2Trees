'''
Created on May 15, 2013

@author: Jeff
'''
import urllib2
from bson.json_util import dumps
import json
import zlib
import time
from dota2.resources.constants import *
import os
from pymongo import MongoClient
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
        #self.growMatchCollection(AllPick, 500, 1110285949)
        #
        # connect to the students database and the ctec121 collection

        #url = "http://api.steampowered.com/ISteamNews/GetNewsForApp/v0001/?format=json&appid=440&count=3"
        #self.heroDict = self.getHeroes()
        
        #req = urllib2.Request("http://api.steampowered.com/IDOTA2Match_<1>/GetMatchDetails/v1?format=json&appid=440&count=3&key="+UserKey) # Create request object from URL
        #req = urllib2.Request("http://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/v1?format=json&appid=440&count=3&key="+UserKey+"&display_name=penguinsmooches&date_min=1368580298&date_max=1368598684") # Create request object from URL
        #req = urllib2.Request("http://api.steampowered.com/IDOTA2Match_570/GetMatchDetails/v1?key="+UserKey+"&format="+OutputFormat+"&match_id=1100279346") # Create request object from URL
        #print "."
        #opener = urllib2.build_opener() # Construct 'opener'
        #print "."
        #jsonObj = opener.open(req) # Grab compressed file from URL with opener
        #print "."
        #decompressed = zlib.decompress(gzippedFile.read(), 16+zlib.MAX_WBITS) # Extract string version of JSON obj
        #tempJSON = json.load(jsonObj) # Convert string version of JSON obj to a JSON obj
        
        # insert the record
        #db.insert(tempJSON["result"])
        #'''
        # find all documents
        connection = MongoClient()
        db = connection["MatchesDB"]["AllPick"]
        db.remove({})
        results = db.find()
        #self.curJSON    = self.getMatchDetails( MatchID=1110285949)
        #print self.curJSON
        #print "hi"
        f   = open("TEST.txt","w")
        for record in results:
            print record
        f.close()
        #print os.getcwd()
        #'''
        
    def getHeroes(self):
        req = urllib2.Request("http://api.steampowered.com/IEconDOTA2_570/GetHeroes/v1?format=json&appid=440&count=3&key="+UserKey+"&display_name=penguinsmooches&skill=3") # Create request object from URL
        opener = urllib2.build_opener() # Construct 'opener'
        jsonObj = opener.open(req) # Grab compressed file from URL with opener
        tempJSON = json.load(jsonObj) # Convert string version of JSON obj to a JSON obj
        heroList = tempJSON['result']['heroes']
        for hero in heroList: 
            self.heroDict[str(hero['id'])] = hero['name']
        return 
    
    def growMatchCollection(self, RequestedGameMode, NumMatchesRequested, StartingMatchID):
        #
        self.curDB              = self.getDatabase("MatchesDB")
        self.curMatch           = None
        #
        if RequestedGameMode == AllPick:
            self.curMatchCollection = self.curDB['AllPick']
        #
        # Somewhere in here search for last match. 
        #
        self.curMatchHistory    = self.getMatchHistory(NumMatchesRequested=NumMatchesRequested, RequestedGameMode=RequestedGameMode)
        #
        f = open("MatchHistoryExample.json", "w")
        for match in self.curMatchHistory["matches"]:
            if len(match["players"]) < 10:
                pass
            else:
                self.curMatch           = self.getMatchDetails(MatchID=match["match_id"])['result']
                time.sleep(1)
                self.curMatchCollection.insert(self.curMatch)
        f.close()
        return
        
    def getDatabase(self, DatabaseName):
        self.client = MongoClient()
        return self.client[DatabaseName]
        
    # Returns 25 most recent, "Very High" skill games
    # Default matches returned is 25
    def getMatchHistory(self, StartingMatchID=None, NumMatchesRequested=1, RequestedGameMode=AllPick):
        #
        if StartingMatchID is not None:
            self.curURL     = GetMatchHistory+"key="+UserKey+"&format="+OutputFormat+"&game_mode="+str(RequestedGameMode)+ \
                              "&start_at_match_id="+str(StartingMatchID)+"&matches_requested="+str(NumMatchesRequested)+"&min_players=10"
        else:
            self.curURL     = GetMatchHistory+"key="+UserKey+"&format="+OutputFormat+"&game_mode="+str(RequestedGameMode)+ \
                              "&matches_requested="+str(NumMatchesRequested)+"&min_players=10"
        #
        self.curJSON    = self.GetJSONFromURL(self.curURL)
        return self.curJSON["result"]
    
    def getMatchDetails(self, MatchID = None):
        #
        if MatchID is not None:
            self.curURL     = GetMatchDetails+"key="+UserKey+"&format="+OutputFormat+"&match_id="+str(MatchID)
        else:
            print "ERROR WILL ROBINSON"
            return
        #
        self.curJSON    = self.GetJSONFromURL(self.curURL)
        return self.curJSON

    def GetJSONFromURL(self, inputURL):
        self.req        = urllib2.Request(inputURL)
        self.opener     = urllib2.build_opener() # Construct 'opener'
        self.WrapJSON   = self.opener.open(self.req) # Grab compressed file from URL with opener
        self.curJSON    = json.load(self.WrapJSON)
        return self.curJSON
    
    

jeff = MyClass()

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
