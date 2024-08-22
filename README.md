# RP-retro-Terminal

This is a roleplaying Terminal for open roleplaying games or for tabletop games in futuristic settings. Easy modability was one of the main concerns during the development, so any user with minimal programming skills can change this terminal for his game and setting

As this Terminal provides various [functionality](#Content), it also provides integration with the messenger of the Game Master or Dungeon Master, so all important events in the terminal will be displayed at his screen no matter GM/DM position

This Terminal still Work In Progress, so any feedback, bugreport, push request or suggestion is highly appreciated

# Examples

# Installation

Installation comes in 3 steps:
1. Install **cool-retro-term**
2. Install **python**
3. Install **python modules**

> [!NOTE]
> Installation tutorial goes for people with low programming knowledge.
> 
> If you feel you can handle it yourself - install cool-retro-term and python modules as more fittable for you

## cool-retro-term

1. Install [windows Terminal](https://apps.microsoft.com/detail/9n0dx20hk701). This part is important, as stock terminal doesn't support shaders and can't make cool retro effect
2. Launch terminal at least once and close it
3. Go to this github (https://github.com/Hammster/windows-terminal-shaders) and download the package (Green button download -> ZIP)
4. Unarchive the `windows-terminal-shaders-main` at `C:/` (If you want to store shaders anywhere else, you will need to change 55 line at settings.json later)
    > Final folder should look like `C:/windows-terminal-shaders-main/`, if you have -master or -1.2.0 at the end - remove it
5. Download RP-retro-Terminal archive and unzip it in any folder you want (you will launch your terminal from this folder as well)
6. Go to `windows-terminal_settings_json` in RP-retro-Terminal and copy file `settings.json`
7. Paste it in this directory `%LocalAppData%\Packages\Microsoft.WindowsTerminal_8wekyb3d8bbwe\LocalState`
    If you don't want to paste the settings like this, you can follow the tutorial from windows-terminal-shaders repository from point 3
8. Launch the Terminal from `⊞Win` and type Terminal, or any other way

If you see cool retro yellow screen - you've done it

> [!TIP]
> For those users who want to use other colors of CRT screen - open `crt.hlsl` file of `windows-terminal-shaders-main` package with **Notepad++** and change this line `#define TINT_COLOR              TINT_AMBER` with one of the options below it

> [!TIP]
> For those users who want to use other shaders - go to `settings.json` from point 7 and change name at `line 55`

> [!WARNING]
> If you don't see the result you wanted to see - follow through [`windows-terminal-shaders-main`](https://github.com/Hammster/windows-terminal-shaders) instruction

## python

1. If you are not sure if there is python at your PC/Laptop/Anything, it's better to open Terminal and write `uninstall python`. Don't worry, we will install it later
2. You can just write `python` in the same Terminal and windows will open Microsoft Store with latest python, or you can just download it [from here](https://apps.microsoft.com/detail/9ncvdn91xzqp?hl=en-us&gl=US)

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

## Telegram bot setup

This section is optional, if you want telegram bot to spam you with messages of player's important activity in the Terminal (like starting self destruct timer, opening passworded file, PINGing an item) - you should create telegram bot (this is easy) and set up `telegram_integration.py` file. Just follow these steps:

1. Write to this bot https://t.me/BotFather
2. Write/push /start
3. Write/push /newbot
4. Write a name for him (usually it's best to write your nickname + _DMbot, like HalfDeady_DM so you can easily understand who is writing to you)
5. Write a name for the bot (name from p.4 + bot, like HalfDeady_DMbot)
6. Copy HTTP API token
7. Open `telegram_integration.py` file and paste this HTTP API TOKEN inside of quotes of `tele_api_key = ''` at the line 3, so it will be like this `tele_api_key = '{YOUR_API_TOKEN}'`
8. Write to this bot https://t.me/username_to_id_bot
9. Write/push /start
10. Copy your ID (it's line of numbers)
11. Open `telegram_integration.py` file and paste your ID inside of quotes of `tele_user_id = ''` at the line 4, so it will be like this `tele_user_id = '123456789'`
12. Open your newly created bot (there's a link to it at BotFather message)
13. Write/push /start . Note that it will not respond to you, as it doesn't work yet, it's totally okay and needed to pass by telegram spam protection
14. Launch your RP-retro-Terminal and try one of the important commands (selfdestruct, service, door, file passworded), and bot will send you the message

## Discord bot setup

Not implemented yet

# Launching

To launch the RP-Terminal your Terminal should be in the same folder. If it's not, use cd `C:/{your_Terminal_folder}` command

Than just `python main.py`

And RP-Terminal should work

If at this point everything works good, you can proceed to play with the RP-Terminal, modify it, try it out, anything

If something went wrong with the python installation - let me know, so i can add additional points to the instruction

# Content

This sections will tell how commands works and how to use them as intended. Currently RP-retro-Terminal supports next console commands:

* **HELP**
* **DIAG**
* **FILE**
* **PING**
* **ITEM**
* **CLEAR**
* **DOOR**
* **ALARM**
* **SERVICE**
* **SELFDESTRUCT**

Every command might be issued without additional parameters, but not all commands will work that way. If command need at least any parameters, command will say that

More detailed help can be found in the help files in hidden_data, all hidden options will be described in sections below the command

Also every command have VERSION attribute that shows fictional version of the utility. It will not be described in the sections below

Exmaples of work of the commands can be found in the youtube video above

## HELP

This is a simple command that reads content of `hidden_data/help.txt` if no parameters transfered, or reads content of `hidden_data/help_{param}.txt` if there is any parameters

Each help file comes in separate file. It's content created as UNIX help reference

If file is not found, command will say that

## DIAG

DIAG command works with `hidden_data/shipdiag.txt` file and have 3 main parameters:

* DIAG ALL
* DIAG LIST
* DIAG {MODULE}

> [!CAUTION]
> This command relies on `breakline` which can be setted up in config. IF you remove the file's header `breakline`s or change it on other `breakline`s - diag command **will** break up, proceed with caution
>
> For more information see [modding](#Modding) section

### DIAG ALL

This command just outputs everything there is `hidden_data/shipdiag.txt` file

### DIAG LIST

Diag list skips 2 `breakline`s and spit out the lines in between of `breakline`s every 2 `breakline`, essentially showing just the names of the sections on ship/station and overall info about the section

### DIAG {PARAM}

This command goes through the file and looks for the first word to match the `{PARAM}`, after what shows contents until hits second `breakline`

## FILE

FILE command work with `hidden_data/files_passwords.txt` and whole `open_data` folder. FILE command has 2 parameters, that can be parsed in:

* FILE LIST
* FILE {FILENAME}

There are also two hidden functions that helps this one work effectively

* FILE TYPE
* FILE PASSWORD

### FILE TYPE

This function transfers file type into lore-accurate format:

* .txt = TEXTLOG
* .ascii = IMAGE
* .wav = AUIDOLOG
* everything else = UNKWN FORMAT

.ascii is basically .txt that was manually renamed to .ascii, and still opens as .txt file 

### FILE PASSWORD

There are two functions, one check if there is password for file, other one checks the file password and if there is one - asks the player for file password

Currently there is an option that makes file check "slow" by making decription progress bar before checking password match, you can turn it on or off in the config part. This was needed it my case, so players won't brute-force all the known passwords

To change/add/remove file passwords you need to open hidden_data/files_passwords.txt and edit passwords in next format:

`{filename} {password}`

> [!IMPORTANT]
> If you add spacebar at the end of the password - it will be part of the password

### FILE LIST 

Writes list of files from `open_data` folder, also writes file type and is it password protected

> [!IMPORTANT]
> Files in subfolders will be ignored

### FILE {FILENAME}

This command reads/plays the `{filename}` file from `open_data` folder if it's one of the supported types (.txt, .ascii, .wav)

If it's .wav this command will also put a progress bar up to length of the wav file

If file requires password (as in `hidden_data/files_passwords.txt`) - password will be asked, and file will be shown on correct password

> [!NOTE]
> There is no need to write full file name in this command. If there are no duplicates, writing `FILE SK_spa` will resuilt in showing file `SK_spare_part.ascii`

> [!NOTE]
> This command is register-sensetive

## PING

This command is a part of ITEM command and shows detailed information, if `{PARAM}` transfered is matching with an entry in `items.csv` file

Basically this programm serves as detailed infromation storage about all mysterious items that players might find and which have some serial_number on them

## ITEM

## CLEAR

Just clears the screen from the mess above, so player can't scroll up until player issues enough commands

## DOOR

## ALARM

## SERVICE

## SELFDESTRUCT

# Modding

## configs

## Removing/Renaming commands

## Changing hidden files

### startup

### shipdiag

### files passwords

### csv files

## audio

## Translation

# Known bugs

## DIAG breakline

If you add spacebar to the end of the breakline, so it will differ from the one in python config - diag command will break. If you want to change breakline in the shipdiag file, you need also change breakline in the config for an exact match

## Spacebar after param

If you write space

# Plans

## Localisation csv

## Discord integration

# Suggestions, Feedbacks and Patches

# Contacts

Ways you can contact me:

* (Telegram)[t.me/HalfDeady]
* Discord - HalfDeady (just add me)
* (email)[halfdeadanarchyst@gmail.com]
* And github

# Credits

[windows-terminal-shaders](https://github.com/Hammster/windows-terminal-shaders) for his exceptional visual base for this terminal. Without these cool graphics RP-retro-Terminal would be less atmospheric than

[@Danieczka](https://github.com/Dane-VI) for massive help with audios of the Terminal

[@jess_jass](t.me/@jess_jass) for making atmospheric audio logs, character dialogues and other narrative for FILE section of the Terminal

[miri-solari](https://github.com/Miri-Solari) for help with DIAG part and other minor tasks

Special thanks for my crew of space sailors for testing this Terminal out

# License

This work is licensed under the Creative Commons Attribution 4.0 International License. ![license-image](https://mirrors.creativecommons.org/presskit/buttons/88x31/png/by-nc.png)

To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/ or send a letter to Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.

## You are free to:

* **Share** — copy and redistribute the material in any medium or format for any purpose, even commercially.
* **Adapt** — remix, transform, and build upon the material for any purpose, even commercially.

The licensor cannot revoke these freedoms as long as you follow the license terms.

## Under the following terms:

* **Attribution** — You must give appropriate credit , provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.

No additional restrictions — You may not apply legal terms or technological measures that legally restrict others from doing anything the license permits.
