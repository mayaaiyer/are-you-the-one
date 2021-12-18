#The number of beams in a match up ceremony (-1 means the ceremony hasn't happened yet)
MATCH_CEREMONY_RESULTS = [3, 3, 4, 4, -1, -1, -1, -1, -1, -1]

#Matches set up at the matching ceremony
MATCHES = dict()
MATCHES["Asaf"] =       ["Francesca",   "Camille",      "Camille",      "Camille"]
MATCHES["Cam"] =        ["Victoria",    "Julia",        "Nicole",       "Emma"]
MATCHES["Cameron"] =    ["Mikayla",     "Mikayla",      "Mikayla",      "Mikayla"]
MATCHES["Giovanni"] =   ["Kaylen",      "Kaylen",       "Kaylen",       "Kaylen"]
MATCHES["John"] =       ["Emma",        "Nicole",       "Victoria",     "Victoria"]
MATCHES["Morgan"] =     ["Julia",       "Alyssa",       "Francesca",    "Tori"]
MATCHES["Prosper"] =    ["Camille",     "Emma",         "Emma",         "Nicole"]
MATCHES["Sam"] =        ["Alyssa",      "Francesca",    "Alyssa",       "Alyssa"]
MATCHES["Stephen"] =    ["Nicole",      "Tori",         "Tori",         "Julia"]
MATCHES["Tyler"] =      ["Tori",        "Victoria",     "Julia",        "Francesca"]

WEEK1 = []
for i in MATCHES.keys():
    WEEK1.append(MATCHES[i][0])
WEEK2 = []
for i in MATCHES.keys():
    WEEK2.append(MATCHES[i][1])
WEEK3 = []
for i in MATCHES.keys():
    WEEK3.append(MATCHES[i][2])
WEEK4 = []
for i in MATCHES.keys():
    WEEK4.append(MATCHES[i][3])
WEEK5 = []
WEEK6 = []
WEEK7 = []
WEEK8 = []
WEEK9 = []
WEEK10 = []

ALLWEEKS = [WEEK1, WEEK2, WEEK3, WEEK4]

TRUTHBOOTH_DENIED = [("Prosper", "Tori"), ("John", "Julia"), ("Asaf", "Tori")]

TRUTHBOOTH_CONFIRMED = [("Cameron", "Mikayla")]
