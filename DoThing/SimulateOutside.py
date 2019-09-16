#!/usr/bin/env python3
import datetime
"""
This just holds functions that simulate the behaviour of other functions
"""
g_file = "samplefilename.jpg"

# ----- title
def getTitle(p_filename):
    return "Generic Title"

def setTitle(p_filename, p_val):
    return True

# ----- artist
def getArtists(p_filename):
    return ["Artist: Jane Doe", "sample artist"]

def setArtists(p_filename, p_val):
    return True

def addArtist(p_filename, p_val):
    return True

def removeArtist(p_filename, p_val):
    return True

# ----- description
def getDesc(p_filename):
    return "Sample test string. Look how long this is. This is supposed to be a description." \
           "I think it's pretty great so far."

def setDesc(p_filename, p_value):
    if len(p_value)>10 or len(p_value)<3:
        return True
    else:
        return False

# ----- tag
def getTags(p_filename):
    return ["sample", "example", "test", "this is a long tag"]

def setTags(p_filename, p_val):
    return True

def addTag(p_filename, p_val):
    return True

def removeTag(p_filename, p_val):
    #print("SimulateOutside.removeTag(",p_filename, ", ", p_val, ")")
    return True

# ----- rating
def containsRating(p_filename):
    return True

def getRating(p_filename):
    return 3

def setRating(p_filename, p_val):
    return True

def wipeRating(p_filename):
    return True

# ----- source url
def getSource(p_filename):
    return "exampleurl/src/1832.jpg"

def setSource(p_filename, p_val):
    return True

# ----- orginal date
#g_originaldate = datetime.datetime(2002, 12, 25, 21, 43, 38)
g_originaldate = None

def containsOrgDate(p_filename):
    return not g_originaldate == None

def getOriginalDate(p_filename):
    print("SimulateOutside.getOriginalDate()", g_originaldate)
    if g_originaldate==None:
        return datetime.datetime(1, 1, 1, 0, 0, 0)
    return g_originaldate

def setOriginalDate(p_filename, p_val):
    print("SimulateOutside.setOriginalDate():", p_val, g_originaldate)
    global g_originaldate
    g_originaldate = p_val
    return True

# ----- series
def containsSeries(p_filename):
    return True

def getSeries(p_filename):
    return ("Sample Quest", 12)

def setSeries(p_filename, p_name, p_ins):
    return True

def wipeSeries(p_filename):
    return True