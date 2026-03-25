import os
from bs4 import BeautifulSoup


# Folder containing the HTML files
folder_path = "C:\\Users\\Ian\\Documents\\Rejuv HTML Pages"

# Loop through all files
for filename in os.listdir(folder_path):
    # Saftey check that we're only going through html files
    if filename.endswith(".html"):
        file_path = os.path.join(folder_path, filename)

        # Open and read file
        with open(file_path, "r", encoding="utf-8") as file:
            html_content = file.read()

        # Parse HTML
        soup = BeautifulSoup(html_content, "html.parser")

        # EXTRACT DATA
        final = {}

        # Moves learned by level up
        moves = {}
        i = 0

        table = soup.find(id="By_leveling_up").parent.next_sibling.next_sibling.find("tbody").contents
        for element in table:
            if(i >= 1):
                moves[i] = element.contents
                moves[i] = list(filter(lambda x: x != '\n', moves[i]))
            i += 1
        

        for value in moves.values():
            move_name = value[1].get_text().strip()
            level = "8L" + value[0].get_text().strip()

            if move_name in final:
                final[move_name].append(level)
            else:
                final[move_name] = [level]

        # Moves learned by TM
        moves = {}
        i = 0

        table = soup.find(id="By_TM").parent.next_sibling.next_sibling.find("tbody").contents
        for element in table:
            if(i >= 1):
                moves[i] = element.contents
                moves[i] = list(filter(lambda x: x != '\n', moves[i]))
            i += 1

        for value in moves.values():
            move_name = value[2].get_text().strip()
            level = "8M"

            if move_name in final:
                final[move_name].append(level)
            else:
                final[move_name] = [level]

        # Moves learned by Tutor
        moves = {}
        i = 0

        table = soup.find(id="By_Tutor").parent.next_sibling.next_sibling.find("tbody").contents
        for element in table:
            if(i >= 1):
                moves[i] = element.contents
                moves[i] = list(filter(lambda x: x != '\n', moves[i]))
            i += 1

        for value in moves.values():
            move_name = value[1].get_text().strip()
            location = value[0].get_text().strip()
            level = "8T"

            if location != "Unavailable":
                if move_name in final:
                    final[move_name].append(level)
                else:
                    final[move_name] = [level]

        # Eggs Moves
        moves = {}
        i = 0

        table = soup.find(id="By_Breeding").parent.next_sibling.next_sibling.find("tbody").contents
        for element in table:
            if(i >= 1):
                moves[i] = element.contents
                moves[i] = list(filter(lambda x: x != '\n', moves[i]))
            i += 1

        for value in moves.values():
            move_name = value[1].get_text().strip()
            level = "8E"

            if move_name in final:
                final[move_name].append(level)
            else:
                final[move_name] = [level]
        
        # Sort List
        sortedFinal = dict(sorted(final.items()))
        print(sortedFinal)


        #TO DO, FIGURE OUT HOW TO ADD IT IN THE RIGHT FORMAT INTO ONE DOCUMENT!!

        # title = soup.title.string if soup.title else "No title"

        # # Example: all links
        # links = [a['href'] for a in soup.find_all('a', href=True)]

        # # Example: all paragraph text
        # paragraphs = [p.get_text(strip=True) for p in soup.find_all('p')]

        # # 🧪 MANIPULATE DATA
        # num_links = len(links)
        # short_paragraphs = [p[:50] for p in paragraphs]

        # # 🖨️ OUTPUT FORMAT
        # print(f"FILE: {filename}")
        # print(f"Title: {title}")
        # print(f"Number of links: {num_links}")
        # print("Sample paragraphs:")
        # for p in short_paragraphs[:3]:
        #     print(f" - {p}")
        # print("=" * 40)