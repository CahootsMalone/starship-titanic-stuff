# Starship Titanic Stuff

Odds and ends related to the 1998 computer game [Starship Titanic](https://en.wikipedia.org/wiki/Starship_Titanic).

## Documentation
* Files for each character containing the captions for all their dialogue:
  * [BarBot](docs/sentences-BarBot.md)
  * [BellBot](docs/sentences-BellBot.md)
  * [DeskBot](docs/sentences-DeskBot.md)
  * [DoorBot](docs/sentences-DoorBot.md)
  * [LiftBot](docs/sentences-LiftBot.md)
  * [Maitre d'Bot](docs/sentences-Maitre-d'Bot.md)
  * [Parrot](docs/sentences-Parrot.md)
  * [Succ-U-Bus](docs/sentences-Succ-U-Bus.md)

## Scripts
* [`dlg-parser.py`](scripts/dlg-parser.py): A Python 3 script to parse the game's `dlg` files, which contain the captions and wave files for character dialogue. It generates Markdown files containing all captions (linked from the *Documentation* section above) and can optionally extract the wave files as well.

## General Notes
* Starship Titanic is available on [GOG](https://www.gog.com/game/starship_titanic); however, as-sold, it's unstable on Windows 10. A better option is to use [ScummVM](https://www.scummvm.org/), which [supports the game](https://wiki.scummvm.org/index.php/Starship_Titanic) (albeit with a few minor bugs). As recommended in ScummVM's documentation [here](https://docs.scummvm.org/en/latest/use_scummvm/game_files.html), you can use [innoextract](https://constexpr.org/innoextract/) to extract the files ScummVM requires from the game's GOG installer without having to go through the installation.
* The [ScummVM Starship Titanic engine](https://github.com/scummvm/scummvm/tree/master/engines/titanic) (SSTE) uses [a binary file called `titanic.dat`](https://github.com/scummvm/scummvm/blob/master/dists/engine-data/titanic.dat) that contains information retrieved from the game's executable. The SSTE code to read this file is [here](https://github.com/scummvm/scummvm/blob/master/engines/titanic/support/files_manager.cpp); the code that generates the file is [here](https://github.com/scummvm/scummvm/blob/master/devtools/create_titanic/create_titanic_dat.cpp).