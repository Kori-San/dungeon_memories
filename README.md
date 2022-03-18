# Dungeon Memories

<i> <b> Dungeon Memories </i> </b> (abbreviated <i> <b> DuMe </i> </b> ) is a Python 3 Script that will help <b> Dungeon Masters </b> to remember many important information about <b> NPCs </b> for their <b> PRPGs </b> by storing and displaying YAML/YML Sheets on a Tkinter Interface.<br>

# Installation and usage

## How to install / run DuMe ?
You can run [./run.sh](https://github.com/Kori-San/dungeon_memories/blob/main/run.sh) in your CLI to check <i> dependencies </i> and install missing ones, after the check you can launch <i> <b> DuMe </i> </b> by running [./run.sh](https://github.com/Kori-San/dungeon_memories/blob/main/run.sh) or [./dungeon_memories.py](https://github.com/Kori-San/dungeon_memories/blob/main/dungeon_memories.py). <br> <br>
I strongly advise you to launch [./run.sh](https://github.com/Kori-San/dungeon_memories/blob/main/run.sh) every time a new release is made in case a new dependencie has been added. <br>

## How to use DuMe ?

After launching DuMe you are invited to select a Sheet from the [./sheets/](https://github.com/Kori-San/dungeon_memories/tree/main/sheets) folder, then click the 'Set' Button, DuMe will automatically refresh the displayed data to match the data of the selected file. <br>

## How to make a DuMe sheet ?

For your YAML/YML Sheets to be recognized you'll need 2 Keys "info" and "stat".
```
info:
  ...
stat:
  ...
```
Only those keys are required for the Tables to be built right, every other Key/Value within them is customizable. <br> <br>
Feel free to check out the [./sheets/template.yaml](https://github.com/Kori-San/dungeon_memories/blob/main/sheets/template.yaml) or the [./sheets/Exemples](https://github.com/Kori-San/dungeon_memories/tree/main/sheets/Exemples) files to see how you can build your own DuMe Sheet.<br>

# About DuMe
## Dependencies
- [os](https://docs.python.org/3/library/os.html)
- [io](https://docs.python.org/3/library/io.html)
- [yaml](https://pyyaml.org/)
- [tkinter](https://docs.python.org/3/library/tkinter.html)

## Issues
Feel free to contact me using the issues tab if you encounter any problem regarding DuMe or if you have a suggestion to make!

## Credits
DuMe | Kori-San | 2022
