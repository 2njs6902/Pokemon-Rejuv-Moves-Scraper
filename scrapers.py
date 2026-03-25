import os
from bs4 import BeautifulSoup
from pathlib import Path



# Moves learned by level up
def getLevelMoves(movesDict : dict, soup : BeautifulSoup):
    """ Scrapes level up moves and adds them to 

    Args:
        movesDict (dict): _description_
        soup (BeautifulSoup): _description_
    """
    movesHTML = {}
    i = 0

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
