import os
from bs4 import BeautifulSoup
from pathlib import Path

FORMS = ["aeviumrocky", "aeviumfiery", "aeviumicy", "alola", "galar", "aevium", "sandcloak", "trashcloak", "midnight", "dusk"] # All the forms 

def checkForm(pokemon : str):
    for form in FORMS:
        if form in pokemon:
            return True

    return False

# Moves learned by level up
def getLevelMoves(pokeDict : dict, name :str, soup : BeautifulSoup, movesDict : dict):
    # If your a pokemon form, skip you
    if(checkForm(name)):
        return
    
    # Otherwise, prepare the variable's we'll need for either of the next loops
    movesHTML = {}
    i = 0
    numForms = len(pokeDict[name][1])
    print(pokeDict[name][1])

    # If your the base pokemon (i.e wormadam grass cloak is the base for sandy cloak and trash cloak)
    if(numForms != 0):
        table = soup.find(id="By_leveling_up").parent.next_sibling.next_sibling
        for k in range(0, numForms + 1):
            if(k == 0):
                tempName = name
            else:
                tempName = pokeDict[name][1][k-1]

            if tempName not in movesDict:
                movesDict[tempName] = {}

            t = 0
            currTable = table.find("tbody").contents
            workingTable = list(filter(lambda x: x != '\n', currTable))

            for element in workingTable:
                movesHTML[i] = element.contents
                movesHTML[i] = list(filter(lambda x: x != '\n', movesHTML[i]))
                i += 1
            print(f"{k}th pokemon's html table is completed")
            for value in movesHTML.values():
                try:
                    move_name = value[1].get_text().strip()
                    if(move_name == "Move"):
                        continue
                    level = "8L" + value[0].get_text().strip()
                
                    if move_name in movesDict[tempName].keys():
                        movesDict[tempName][move_name].append(level)
                    else:
                        movesDict[tempName][move_name] = [level]  
                except:
                    continue
            print(f"{k}th pokemon was added to movesDict")
            print(movesDict)
            movesHTML = {}
            i = 0
            table = table.next_sibling.next_sibling.next_sibling.next_sibling
            

    #You dont got forms  THIS NEEDS TO BE FIXED WITH NEW MOVES DICTIOANRY LOGIC (The last bit when ur iterating through values in html, just change how they added to list)
    else:
        table = soup.find(id="By_leveling_up").parent.next_sibling.next_sibling.find("tbody").contents
        table = list(filter(lambda x: x != '\n', table))

        for element in table:
            movesHTML[i] = element.contents
            movesHTML[i] = list(filter(lambda x: x != '\n', movesHTML[i]))
            i += 1

        for value in movesHTML.values():
            move_name = value[1].get_text().strip()
            level = "8L" + value[0].get_text().strip()

            if move_name in movesDict:
                movesDict[move_name].append(level)
            else:
                movesDict[move_name] = [level]

# Moves learned by TM
def getTMMoves(movesDict : dict, soup : BeautifulSoup):
    # If your a pokemon form, skip you
    if(checkForm(name)):
        return
    
    movesHTML = {}
    i = 0

    table = soup.find(id="By_TM").parent.next_sibling.next_sibling.find("tbody").contents
    table = list(filter(lambda x: x != '\n', table))

    for element in table:
        movesHTML[i] = element.contents
        movesHTML[i] = list(filter(lambda x: x != '\n', movesHTML[i]))
        i += 1

    for value in movesHTML.values():
        move_name = value[2].get_text().strip()
        level = "8M"

        if move_name in movesDict:
            movesDict[move_name].append(level)
        else:
            movesDict[move_name] = [level]

# Moves learned by Tutor
def getTutorMoves(movesDict : dict, soup : BeautifulSoup):
    movesHTML = {}
    i = 0

    table = soup.find(id="By_Tutor").parent.next_sibling.next_sibling.find("tbody").contents
    table = list(filter(lambda x: x != '\n', table))

    for element in table:
        movesHTML[i] = element.contents
        movesHTML[i] = list(filter(lambda x: x != '\n', movesHTML[i]))
        i += 1

    for value in movesHTML.values():
        move_name = value[1].get_text().strip()
        location = value[0].get_text().strip()
        level = "8T"

        if location != "Unavailable":
            if move_name in movesDict:
                movesDict[move_name].append(level)
            else:
                movesDict[move_name] = [level]

# Eggs Moves
def getEggMoves(movesDict : dict, soup : BeautifulSoup):
    movesHTML = {}
    i = 0

    table = soup.find(id="By_Breeding").parent.next_sibling.next_sibling.find("tbody").contents
    table = list(filter(lambda x: x != '\n', table))

    for element in table:
        movesHTML[i] = element.contents
        movesHTML[i] = list(filter(lambda x: x != '\n', movesHTML[i]))
        i += 1

    for value in movesHTML.values():
        move_name = value[1].get_text().strip()
        level = "8E"

        if move_name in movesDict:
            movesDict[move_name].append(level)
        else:
            movesDict[move_name] = [level]

def getAllMoves(movesDict : dict, soup : BeautifulSoup):
    getLevelMoves(movesDict, soup)
    getTMMoves(movesDict, soup)
    getTutorMoves(movesDict, soup)
    getEggMoves(movesDict, soup)