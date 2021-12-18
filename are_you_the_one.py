import itertools
import pickle
from parameters import *

boys = list(MATCHES.keys())
boys.sort()
print(boys)

girls = list()
for i in MATCHES.keys():
    girls.append(MATCHES[i][1])
girls.sort()
print(girls)

# returns the number of matches in common between two match lists
def correlation(list1, list2):
    total = 0
    for i in range(len(list1)):
        if list1[i] == list2[i]:
            total = total + 1
    return total

# returns whether a matchlist breaks a rule
def isImpossible(matchlist):
    for match in TRUTHBOOTH_DENIED:
        if (matchlist[boys.index(match[0])] == match[1]):
            return True
    for match in TRUTHBOOTH_CONFIRMED:
        if (matchlist[boys.index(match[0])] != match[1]):
            return True
    for week in ALLWEEKS:
        if correlation(matchlist, week) != MATCH_CEREMONY_RESULTS[ALLWEEKS.index(week)]:
            return True        
    return False           

#list of possible matches
possible = []

iterable = itertools.permutations(girls,len(girls))
for matching in iterable:
    # skip match lists that break a rule
    if isImpossible(matching):
        continue
    else:
        possible.append(matching)
        
print("There are " + str(len(possible)) + " possible matchings after " + str(len(ALLWEEKS)) + " weeks!")

def printRemaining():
    for matching in possible:
        printString = ""
        for i in range(len(matching)):
            printString = printString + ("("+boys[i]+", " + matching[i]+ ")")
        print(printString)
        print("")

def makePercent(n):
    return (float(n) / len(possible))*100

#Determine the odds of a blackout
# What percent of remaining possible matchings contain 0 of this week's couples?
beamDistribution = [0] * (len(girls)+1)
for matching in possible:
    commonCount = correlation(matching, ALLWEEKS[len(ALLWEEKS) - 1])
    beamDistribution[commonCount] = beamDistribution[commonCount] + 1

mostLikelyBeamCount = 0
maxBeamCount = 0
highestBeamIndex = 0
lowestBeamIndex = 0
for i in range(0, len(beamDistribution)):
    beamCount = beamDistribution[i]
    if beamCount != 0:
        highestBeamIndex = i
    if beamCount > maxBeamCount:
        maxBeamCount = beamCount
        mostLikelyBeamCount = i
for i in range(0, len(beamDistribution)-1):
    beamCount = beamDistribution[i]
    if beamCount != 0:
        lowestBeamIndex = i
        break

#excludes truth booth perfect matches
blackOutPercent = makePercent(beamDistribution[len(TRUTHBOOTH_CONFIRMED)])

distString = ''
for i in range(0, len(beamDistribution)):
    distString = distString + ', '+ str(makePercent(beamDistribution[i]))[:str(makePercent(beamDistribution[i])).index('.')]+'%'

#Print tweet format
print('Beam Probabilities: [' + distString[2:] + ']')
print('Most likely Beam Count: ' + str(mostLikelyBeamCount))
#print('Max Beam Count: ' + str(highestBeamIndex))
print('Blackout Odds: ' + str(blackOutPercent)+'%')

print('')



match_dictionary = {}
for guy in boys:
    match_dictionary[guy] = [0] * len(girls)

# fill in dictionary
for matching in possible:
    for guy in boys:
        match_dictionary[guy][girls.index(matching[boys.index(guy)])] += float(1)/len(possible)

#determine best matching
def determineBestMatching():
    best_match_score = 0
    best_matching = []
    for matching in possible:
        score = 0
        for guy in boys:
            score += match_dictionary[guy][girls.index(matching[boys.index(guy)])]
        #print("score " + str(score))
        if score > best_match_score:
            best_match_score = score
            best_matching = matching
    print("Best score " + str(best_match_score))

    best_string = ""
    for i in range(len(best_matching)):
        best_string += '''||style="background:#CFCFCF"|''' + """'''"""+ boys[i] + ", " +best_matching[i]+"""'''"""
    return best_string

def printBestMatching():
    best_string = determineBestMatching()
    print('''{| class="wikitable"''')
    print("|-")
    print(best_string[1:])
    print("""|}""")

#print all remaining scores
def printAllScores():
    for matching in possible:
        score = 0
        for guy in boys:
            score += match_dictionary[guy][girls.index(matching[boys.index(guy)])]
        print("Score " + str(score))
        printString = ""
        for i in range(len(matching)):
            printString = printString + ("("+boys[i]+", " + matching[i]+ ")")
        print(printString)
        print("")

# prints the percent of possible matchings that contain each couple
def printAll():
    for key in sorted(match_dictionary.keys()):
        print(key.upper())
        matchPercents = ""
        for i in range(len(match_dictionary[key])):
            matchPercents += " " + str(girls[i]) + " " + "%.1f%%" % (100*match_dictionary[key][i])
        print(matchPercents)

#prints the top match for each guy
def printMaxBoys():
    for key in sorted(match_dictionary.keys()):
        print(key.upper())
        matchPercents = ""
        maxPercent = 0
        maxIndex = 0
        for i in range(len(match_dictionary[key])):
            percent = match_dictionary[key][i]
            if percent > maxPercent:
                maxPercent = percent
                maxIndex = i
        
        matchPercents += " " + str(girls[maxIndex]) + " " + "%.1f%%" % (100*match_dictionary[key][maxIndex])
        print(matchPercents)

#prints the top match for each girl
def printMaxGirls():
    for i in range(len(boys)):
        print(girls[i].upper())
        maxPercent = 0
        maxIndex = 0
        matchPercents = ""
        for key in sorted(match_dictionary.keys()):
            percent = match_dictionary[key][i]
            if percent > maxPercent:
                maxPercent = percent
                maxIndex = key

        matchPercents += " " + str(maxIndex) + " " + "%.1f%%" % (100*match_dictionary[maxIndex][i])
        print(matchPercents)

print("BOYS MATCHES")
printMaxBoys()

print("\n")

print("GIRLS MATCHES")
printMaxGirls()