import requests
from bs4 import BeautifulSoup

BASE_LINK = "https://rejuvenation.wiki.gg" # The base for all links 
FORMS = [ # All the forms
    ("aevianrocky", "aeviumrocky"),
    ("aevianfiery", "aeviumfiery"),
    ("aevianicy", "aeviumicy"),
    ("alolan", "alola"),
    ("galarian", "galar"),
    ("aevian", "aevium"),
    ("sandcloak", "sandy"),
    ("trashcloak", "trash"),
    ("midnight", "midnight"),
    ("dusk", "dusk")
]

def makePokemonDictionary(webpage : str):
    """ Create a dictionary of pokemon that are obtainable in Pokemon Rejuvenation

    Args:
        webpage (str): Link to webpage that contains a table of all the pokemon, should be "https://rejuvenation.wiki.gg/wiki/Pok%C3%A9mon_Locations"

    Returns:
        pokemonDictionary (dict) : Key = Pokemon name, value = List that contains a link to it's Rejuvenation wiki page, a boolean on whether that pokemon has regional forms, and a list containing each form's name
    """
    # Getting HTML page
    response = requests.get(webpage)
    soup = BeautifulSoup(response.text, "html.parser")

    # From the table body, get a list of the table body contents, being each row of the table, and strip out all the "/n" from the list
    table = soup.find("tbody").contents
    table = list(filter(lambda x: x != '\n', table))
    
    pokemonDictionary = {}
    i = 0

    for element in table:
        # Skip the first element of the list cause it's blank for whatever reason
        if(i >= 1):
            rowData = element.contents
            rowData = list(filter(lambda x: x != '\n', rowData))

            name = rowData[2].get_text().strip().lower().replace(" ", "")

            # Don't add the pokemon if it isn't obtainable
            if('Not Obtainable' == rowData[5].get_text().strip()):
                i -= 1
                continue
            
            # Retrieving webpage
            a_tag = rowData[2].find('a')
            href = a_tag['href']
            link = BASE_LINK + href

            # Adding the pokemon's member variables
            pokemonDictionary[name] = [link]
            pokemonDictionary[name].append([])

            # Processing pokemon in an alternate fashion if they are a regional form
            for key, value in FORMS:
                if(name == "duskull" or name == "dusknoir"):
                    break
                if(name == "lycanrocmidday"):
                    pokemonDictionary["lycanroc"] = pokemonDictionary.pop(name)
                    break
                if key in name:
                    processForm(pokemonDictionary, name, key)
                    break
        i += 1

    return pokemonDictionary

def processForm(pokemonDictionary : dict, name : str, form : str):
    """ Where regional forms are processed into the list

    Args:
        pokemonDictionary (dict): The main dictionary all the pokemon are stored in
        name (str): Full unedited name of the regional form
        form (str): The type of regional form

    Raises:
        KeyError: When the baseform is not found in pokemonDictionary

    Returns:
        properName (str) : The base name (species name) of the pokemon + the proper identifier (alola,galar, etc.)
    """
    baseName = name.replace(form, "")
    
    if baseName not in pokemonDictionary:
        raise KeyError(f"{baseName} not found in pokemonDictionary")

    for key, value in FORMS:
        if (form == key):
            pokemonDictionary[baseName][1].append(baseName + value)
            pokemonDictionary[baseName + value] = pokemonDictionary.pop(baseName + key)