# EpicRanker

A tool to get your current epic game library to get ranked by metascore.

## Pre-reqs

Make sure you have the latest [python3 with pip](https://www.python.org/downloads/) installed.

Install [legendary](https://github.com/derrod/legendary) to be able to parse your epic games library.

Then produce the game_list.txt file by entering the following line to the terminal/cmd/git bash:

```bash
legendary list > game_list.txt
```

## Usage

Run the ranker.py

```bash
python ranker.py
```
## Result

You will see progress and result in termnal.

## Games with not working links

In the result you might see some games labeled as *Incorrect link parsing*. If you want to get scores for these games, you will have to manually upload the metacritic links for them in the *override_links.txt* file. The format is as follows 

>App_id;https://www.metacritic.com/game/my-game/

You can find the app ids in game_list.txt file.

## License

[MIT](https://choosealicense.com/licenses/mit/)