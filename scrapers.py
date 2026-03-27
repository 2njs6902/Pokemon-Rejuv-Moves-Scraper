import os
from bs4 import BeautifulSoup
from pathlib import Path
import requests

FORMS = ["aeviumrocky", "aeviumfiery", "aeviumicy", "alola", "galar", "aevium"] # All the forms 

def checkForm(pokemon : str):
    for form in FORMS:
        if form in pokemon:
            return True

    return False


# Moves learned by level up
def getLevelMoves(pokemonDict : dict, name : str, movesDict : dict):
    #Getting HTML page
    response = requests.get(pokemonDict[name][0])
    soup = BeautifulSoup(response.text, "html.parser")

    #If the pokemon IS a form, skip it
    if(checkForm(name)):
        return
    #If the pokemon doesn't have any forms continue as normally
    if(len(pokemonDict[name][1]) == 0):
        movesHTML = {}
        i = 0

        table = soup.find(id="By_leveling_up").parent.next_sibling.next_sibling.find("tbody").contents
        table = list(filter(lambda x: x != '\n', table))

        for element in table:
            movesHTML[i] = element.contents
            movesHTML[i] = list(filter(lambda x: x != '\n', movesHTML[i]))
            i += 1
        
        for element in table:
            cols = element.find_all(["td", "th"])

            if len(cols) < 2:
                continue

            level = "8L" + cols[0].get_text(strip=True)
            move_name = cols[1].get_text(strip=True)

            if move_name in movesDict:
                movesDict[move_name].append(level)
            else:
                movesDict[move_name] = [level]
    #If the pokemon does have forms do specia version TO DO TO DO
    else:
        movesHTML = {}
        i = 0

        table = soup.find(id="By_leveling_up").parent.next_sibling.next_sibling.find("tbody").contents
        table = list(filter(lambda x: x != '\n', table))

        print(table)

    

# Moves learned by TM
def getTMMoves(movesDict : dict, soup : BeautifulSoup):
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
