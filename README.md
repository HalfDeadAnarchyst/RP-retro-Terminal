# RP-retro-Terminal

This is a roleplaying Terminal for open roleplaying games or for tabletop games in futuristic settings. Easy modability was one of the main concerns during the development, so any user with minimal programming skills can change this terminal for his game and setting

As this Terminal provides various [functionality](README.md/Content), it also provides integration with the messenger of the Game Master or Dungeon Master, so all important events in the terminal will be displayed at his screen no matter GM/DM position

This Terminal still Work In Progress, so any feedback, bugreport, push request or suggestion is highly appreciated

# Installation

Installation comes in 3 steps:
1. Install cool-retro-term
2. Install python
3. Install python modules

## cool-retro-term

1. Install [windows Terminal](https://apps.microsoft.com/detail/9n0dx20hk701). This part is important, as stock terminal doesn't support shaders and can't make cool retro effect
2. Launch terminal at least once and close it
3. Go to this github (https://github.com/Swordfish90/cool-retro-term) and download the package (Green button download -> ZIP)
4. Unarchive the cool-retro-term-master at `C:/` (If you want to store shaders anywhere else, you will need to change 55 line at settings.json later)
5. Download RP-retro-Terminal archive and unzip it in any folder you want (you will launch your terminal from this folder as well)
6. Go to `cool-retro-term_settings_json` in RP-retro-Terminal and copy file `settings.json`
7. Paste it in this directory `%LocalAppData%\Packages\Microsoft.WindowsTerminal_8wekyb3d8bbwe\LocalState`
    If you don't want to paste the settings like this, you can follow the tutorial from cool-retro-term repository from point 3
8. Launch the Terminal from `⊞Win` and type Terminal, or any other way

This is it! If you see cool retro yellow screen - you've done it

For those users who want to use other colors of CRT screen - open `crt.hlsl` file of `cool-retro-term` package with **Notepad++** and change this line `#define TINT_COLOR              TINT_AMBER` with one of the options below it

For those users who want to use other shaders - go to `settings.json` from point 7 and change name at `line 55`

If you don't see the result you wanted to see - follow through `cool-retro-term` instruction

## python

1. If you are not sure if there is python at your PC/Laptop/Anything, it's better to open Terminal and write `uninstall python`. Don't worry, we will install it later
2. You can just write python in the same Terminal and windows will open Microsoft Store with latest python, or you can just download it [from here](https://apps.microsoft.com/detail/9ncvdn91xzqp?hl=en-us&gl=US)

After you done - you have python on your PC/Laptop!

## python modules

Last but not least - install modules, and here we need to learn some terminal commands and controls

`cd PATH` allows you to move between folders in the Terminal. For an example `cd C:/AlienRPG/RP-retro-Terminal` will move you to the terminal in your AlienRPG folder

hint: using `⇥ tab` while writing name auto-fills it, so there's no need to write name of the folder fully!

1. In Terminal go to your RP-Terminal folder (for an example `C:/RP-retro-Terminal`)
2. Write `pip install -r .\requirements.txt`

Alternatively, if you installing packages from somewhere else, you can write these commands. If you already issued `pip install -r .\requirements.txt` - there is no need to write commands below

1. `pip install pygame`
2. `pip install tqdm`
3. `pip install pytelegrambotapi`

You're good!

# Launching

Finally, let's test if it works

To launch the RP-Terminal your Terminal should be in the same folder

Than just `python main.py`

And RP-Terminal should work

If at this point everything works good, you can proceed to play with the RP-Terminal, modify it, try it out

If something went wrong with the python installation - let me know, so i can add additional points to the instruction

# Content

# Modding

# Suggestions, Feedbacks and Patches

# Contacts

# Credits

[Cool-retro-term](https://github.com/Swordfish90/cool-retro-term) for his exceptional visual base for this terminal. Without these cool graphics RP-retro-Terminal would be less atmospheric than

@Danieczka for massive help with audios of the Terminal

@jess_jass for making atmospheric audio logs, character dialogues and other narrative for FILE section of the Terminal

[miri-solari](https://github.com/Miri-Solari) for help with DIAG part and other minor tasks

Special thanks for my crew of space sailors for testing this Terminal out

# License
