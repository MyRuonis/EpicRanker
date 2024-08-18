import requests
import time

def construct_link(game):
    base_link = "https://www.metacritic.com/game/"
    remove = [':', '(', ')', '\'']
    for item in remove:
        game = game.replace(item, '')
    return base_link + game.lower().replace(" ", "-") + "/"

headermap = {"User-Agent": "Mac Firefox"}
override_file = "override_links.txt"
overrides = {}
games_file = "game_list.txt"
game_count = 0
metascore_span = '<span data-v-4cdca868>'
end_span = "</span>"
title_header = "<h1>"

f = open("game_list.txt", "r")
line_count = len(f.readlines())
f.close()

with open(override_file) as file:
    for line in file:
        line = line.split(';')
        overrides[line[0]] = line[1]

metascore = []

id = 0
with open(games_file) as file:
    for line in file:
        print(f'{id/line_count * 100:.2f}%')
        id += 1
        
        line = line.strip()
        
        if not line or line[0] != '*':
            continue
        
        game_count += 1
        line = line.split(" (App name: ")
        line[0] = line[0][2:]
        line[1] = line[1].split(" | ")[0]
        print(line[0] + " | " + line[1])
        
        link = ""
        print(line[1])
        if line[1] in overrides.keys():
            link = overrides[line[1]]
        else:
            link = construct_link(line[0])
        print(link)
        
        info = requests.get(link, headers=headermap, timeout=60).text
        
        if info.find(metascore_span) != -1:
            info = info[info.find(metascore_span) + len(metascore_span):]
            info = info[:info.find(end_span)]
            metascore.append([int(info.replace('.', '').replace('tbd', '0')), line[0]])
        elif info.find(title_header) != -1:
            metascore.append([0, line[0]])
        else:
            metascore.append([-1, line[0]])
 
metascore.sort(reverse=True)

print("Metascore ranking:")
print("\n".join([f'{item[0]} {item[1]}' for item in metascore if item[0] > 0]))
print("\nNo Metascore:")
print([item[1] for item in metascore if item[0] == 0])
print("\nIncorrect link parsing:")
print([item[1] for item in metascore if item[0] == -1])
