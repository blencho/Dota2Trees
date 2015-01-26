'''
Created on Dec 21, 2014

@author: Jeff
'''
# mongo_hello_world.py
# Author: Bruce Elgort
# Date: March 18, 2014
# Purpose: To demonstrate how to use Python to
# 1) Connect to a MongoDB document collection
# 2) Insert a document
# 3) Display all of the documents in a collection

from pymongo import MongoClient

# connect to the MongoDB on MongoLab
# to learn more about MongoLab visit http://www.mongolab.com
# replace the "" in the line below with your MongoLab connection string
# you can also use a local MongoDB instance
connection = MongoClient()

# connect to the students database and the ctec121 collection
db = connection.students.ctec121

# create a dictionary to hold student documents
""
# create dictionary
match_record = {}

# insert the record
db.insert(match_record)

# find all documents
results = db.find()

print()
print('+-+-+-+-+-+-+-+-+-+-+-+-+-+-')

# display documents from collection
for record in results:
    # print out the document
    print record['name'] + ',',record['grade']
    print "\n"

# close the connection to MongoDB
connection.close = db.test
#
#
#
#
##
#
#
#
#
#
#