import os
import json
from bs4 import BeautifulSoup
from pathlib import Path
from webNav import makePokemonDictionary
from scrapersProper import getLevelMoves
import requests
import time
import random

# Path to this Python file
BASE_DIR = Path(__file__).resolve().parent

# Find/Initialize output folder
OUTPUT_DIR = BASE_DIR / "Output" 

# Rejuvenation Pokedex Page
pokedexLink = "https://rejuvenation.wiki.gg/wiki/Pok%C3%A9mon_Locations"

pkDict = makePokemonDictionary(pokedexLink)

moves = {}

with open(OUTPUT_DIR / "wormadam.txt", "r", encoding="utf-8") as f:
    content = f.read()

soup = BeautifulSoup(content, "html.parser")
print(pkDict["wormadam"])
getLevelMoves(pkDict, "wormadam", soup, moves)

print(moves)






# keys = list(pkDict.keys())
# FORMS = ["aeviumrocky", "aeviumfiery", "aeviumicy", "alola", "galar", "aevium", "sandcloak", "trashcloak", "eastsea", "pom-pomstyle", "pa'ustyle", "sensustyle", "midnight", "dusk"] # All the forms 

# def checkForm(pokemon : str):
#     for form in FORMS:
#         if form in pokemon:
#             return True

#     return False

# def fetch_with_retry(url, retries=5):
#     for attempt in range(retries):
#         try:
#             response = requests.get(url, timeout=10)

#             if response.status_code == 200:
#                 return response

#             print(f"Status {response.status_code}, retrying...")
        
#         except requests.exceptions.RequestException as e:
#             print(f"Error: {e}")

#         # exponential backoff
#         wait = 2 ** attempt
#         print(f"Waiting {wait}s...")
#         time.sleep(wait)

#     return None

# i = 777
# for pokemon in pkDict:
#     print(f"{i}: {keys[i]}")
#     if(checkForm(pokemon)):
#         continue
#     response = fetch_with_retry(pkDict[pokemon][0])

#     if response is None:
#         print(f"Skipping {pokemon} (failed after retries)")
#         continue

#     soup = BeautifulSoup(response.text, "html.parser")
#     with open(OUTPUT_DIR / (pokemon + ".txt"), "w", encoding="utf-8") as f:
#         f.write("\n".join(str(row) for row in soup))
#     i += 1
#     time.sleep(random.uniform(2, 5))
