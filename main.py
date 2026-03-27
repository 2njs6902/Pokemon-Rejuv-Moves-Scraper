import os
import json
from bs4 import BeautifulSoup
from pathlib import Path
from webNav import makePokemonDictionary
from scrapers import getLevelMoves

# Path to this Python file
BASE_DIR = Path(__file__).resolve().parent

# Find/Initialize output folder
OUTPUT_DIR = BASE_DIR / "Output" 

# Rejuvenation Pokedex Page
pokedexLink = "https://rejuvenation.wiki.gg/wiki/Pok%C3%A9mon_Locations"

pkDict = makePokemonDictionary(pokedexLink)

moves = {}

i = 0
for pokemon in pkDict:
    print(i)
    print(pokemon)
    getLevelMoves(pkDict, pokemon, moves)
    i += 1
    if(i > 30):
        break


# TODO

# With webNav done, you have a dict of the pokemon. Make a loop that goes through each pokemon, and using the list in the value's list, extract its move data.
# If the form boolean is true, count how many pokemon forms your reading for in this page and make an alternate path for the scraper functions to then deal reading multiple
# learnsets



# FIGURE OUT HOW TO ADD IT IN THE RIGHT FORMAT (JSON) INTO ONE DOCUMENT!!