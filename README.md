# RP-retro-Terminal

This is a roleplaying Terminal for open roleplaying games or for tabletop games in futuristic settings. Easy modability was one of the main concerns during the development, so any user with minimal programming skills can change this terminal for his game and setting

As this Terminal provides various [functionality](#Content), it also provides integration with the messenger of the Game Master or Dungeon Master, so all important events in the terminal will be displayed at his screen no matter GM/DM position

This Terminal still Work In Progress, so any feedback, bugreport, push request or suggestion is highly appreciated

# Examples

TODO: Past youtube link and screenshots here

# Table of contents:

* **[Installation](#installation)**<br>
    * **[cool-retro-term](#cool-retro-term)**<br>
    * **[python](#python)**<br>
    * **[python modules](#python-modules)**<br>
    * **[Telegram bot setup](#telegram-bot-setup)**<br>
    * **[Discord bot setup](#discord-bot-setup)**<br>
* **[Launching](#launching)**<br>
* **[Content](#content)**<br>
    * **[HELP](#help)**<br>
    * **[DIAG](#diag)**<br>
        * **[DIAG ALL](#diag-all)**<br>
        * **[DIAG LIST](#diag-list)**<br>
        * **[DIAG PARAM](#diag-param)**<br>
        * **[DIAG file format](#diag-file-format)**<br>
    * **[FILE](#file)**<br>
        * **[FILE TYPE](#file-type)**<br>
        * **[FILE PASSWORD](#file-password)**<br>
        * **[FILE LIST](#file-list)**<br>
        * **[FILE {FILENAME}](#file-filename)**<br>
        * **[FILE folder](#file-folder)**<br>
    * **[PING](#ping)**<br>
    * **[ITEM](#item)**<br>
        * **[ITEM csv](#item-csv)**<br>
    * **[CLEAR](#clear)**<br>
    * **[DOOR](#door)**<br>
        * **[DOOR LIST](#door-list)**<br>
        * **[DOOR STATUS](#door-status)**<br>
        * **[DOOR OPEN {DOORNAME}](#door-open-doorname)**<br>
        * **[DOOR CLOSE {DOORNAME}](#door-close-doorname)**<br>
        * **[DOOR LOCK {DOORNAME}](#door-lock-doorname)**<br>
        * **[DOOR UNLOCK {DOORNAME}](#door-unlock-doorname)**<br>
    * **[ALARM](#alarm)**<br>
    * **[SERVICE](#service)**<br>
        * **[SERVICE csv](#service-csv)**<br>
        * **[SERVICE ON/ENABLE {SERVICE_NAME}](#service-onenable-service_name)**<br>
        * **[SERVICE OFF/DISABLE {SERVICE_NAME}](#service-offdisable-service_name)**<br>
        * **[SERVICE STATUS {SERVICE_NAME}](#service-status-service_name)**<br>
        * **[SERVICE LIST](#service-list)**<br>
    * **[SELFDESTRUCT](#selfdestruct)**<br>
        * **[SELFDESTRUCT TIMER](#selfdestruct-timer)**<br>
        * **[SELFDESTRUCT START/INITIATE](#selfdestruct-startinitiate)**<br>
        * **[SELFDESTRUCT STOP/ABORT](#selfdestruct-stopabort)**<br>
        * **[SELFDESTRUCT STATUS](#selfdestruct-status)**<br>
        * **[SELFDESTRUCT EXPLODE](#selfdestruct-explode)**<br>
* **[Modding](#modding)**<br>
    * **[Removing/Renaming commands](#removingrenaming-commands)**<br>
    * **[Changing hidden files](#changing-hidden-files)**<br>
        * **[startup](#startup)**<br>
        * **[shipdiag](#shipdiag)**<br>
        * **[files passwords](#files-passwords)**<br>
        * **[csv files](#csv-files)**<br>
    * **[audio](#audio)**<br>
    * **[Translation](#translation)**<br>
* **[Known bugs](#known-bugs)**<br>
    * **[DIAG breakline](#diag-breakline)**<br>
* **[Plans](#plans)**<br>
    * **[Discord integration](#discord-integration)**<br>
* **[Contacts](#contacts)**<br>
* **[Credits](#credits)**<br>
* **[License](#license)**<br>

# Installation

Installation comes in 3 steps:
1. Install `cool-retro-term`
2. Install `python`
3. Install `python modules`

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

* **[HELP](#help)**<br>
* **[DIAG](#diag)**<br>
* **[FILE](#file)**<br>
* **[PING](#ping)**<br>
* **[ITEM](#item)**<br>
* **[CLEAR](#clear)**<br>
* **[DOOR](#door)**<br>
* **[ALARM](#alarm)**<br>
* **[SERVICE](#service)**<br>
* **[SELFDESTRUCT](#selfdestruct)**<br>

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

* **DIAG ALL**
* **DIAG LIST**
* **DIAG {MODULE}**

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

### DIAG file format

1. breakline
2. header information
3. breakline
4. module
5. breakline
6. module content
7. breakline

repeat points 4-7 until done 

## FILE

FILE command work with `hidden_data/files_passwords.txt` and whole `open_data` folder. FILE command has 2 parameters, that can be parsed in:

* **FILE LIST**
* **FILE {FILENAME}**

There are also two hidden functions that helps this one work effectively

* **FILE TYPE**
* **FILE PASSWORD**

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

> [!TIP]
> Example of usage: just write password when programm asks

### FILE LIST

Writes list of files from `open_data` folder, also writes file type and is it password protected

> [!TIP]
> Example of usage `file list`

> [!IMPORTANT]
> Files in subfolders will be ignored

### FILE {FILENAME}

This command reads/plays the `{filename}` file from `open_data` folder if it's one of the supported types (.txt, .ascii, .wav)

If it's .wav this command will also put a progress bar up to length of the wav file

If file requires password (as in `hidden_data/files_passwords.txt`) - password will be asked, and file will be shown on correct password

> [!TIP]
> Example of usage `file captain_log`

> [!NOTE]
> There is no need to write full file name in this command. If there are no duplicates, writing `FILE SK_spa` will resuilt in showing file `SK_spare_part.ascii`

> [!NOTE]
> This command is register-sensetive

### FILE folder

Everything you put in `open_data` folder will be shown (except for other folders)

Only .txt, .ascii (which is renamed .txt) and .wav can be read by the Terminal

If you editing some texts, you don't need to restart Terminal to check FILE READ, as Terminal doesn't store files in the memory. That also means that you potentially can just add files from presaved folders to open_data when players find some flash drives or databanks without restarting the Terminal

## PING

for ping csv file look item csv section

This command is a part of ITEM command and shows detailed information, if `{PARAM}` transfered is matching with an entry in `items.csv` file

Basically this command serves as detailed infromation storage about all mysterious items that players might find and which have some serial_number on them

> [!TIP]
> For an example players found mysterious CARGO_666 crate, player can use `ping CARGO_666` and recieve detailed information about this crate, contents and other notes

## ITEM

ITEM is a command that allows to "scan" particular zone of the ship/station/colony or particular owner

This command serves as vague hint for the players to which zones they should investigate first, and mostly it should show only valuable items (keys, weapons, cargo, buttons) that is tracked by the system

Works well with PING command puzzles

> [!TIP]
> Example of usage `item zone CARGO` or `item owner captain_name`

### ITEM csv

You can access ITEM csv file by [this link](https://docs.google.com/spreadsheets/d/1J50qlpazz9-BZ9HpLJa7esmqiXov2bYRm--KeePo9i4/edit?gid=0#gid=0)

> [!WARNING]
> When you save this file into the hidden_files folder, you ALWAYS should name it `items.csv`

ITEM csv file consists of next headers:

1. **Name** - this field doesn't shows in ITEM command and only used for PING command, when player encountered an item themselves
2. **Type** - doesn't affect anything, just shows in PING as part of the item
3. **Category** - While ITEM command is issued, this one is used to summarize items by Category. For an example, if you have 2 items of category FOOD with Entries 2 and 3, ITEM will show sum of 5
4. **Zone** - used in ITEM command to show items in the current zone
5. **Biolock** - info for players, does this item requires authentification (finger, DNA, pass, anything)
6. **Owner** - used in ITEM command to show items of ther current owner
7. **Status** - info for the players in PING
8. **Entries** - amount of similiar items in the zone, used for p.3 to summarize the info
9. **Note** - additional info for the players in PING

While ITEM doesn't show full information, PING show everything about the one particular item

## CLEAR

Just clears the screen from the mess above, so player can't scroll up until player issues enough commands

## DOOR

This command works well with telegram_integration, where GM/DM can see with which doors player interacts. One of the most complex commands in the Terminal. Options:

1. **List** - shows list of visible doors
2. **Status** - shows all detailed info about current door
3. **Open** - open unlocked door if not broken
4. **Close** - close unlocked door if not broken
5. **Lock** - locks door if not broken
6. **Unlock** - unlocks door if not broken

Also some doors require password to operate with

### DOOR csv

You can access DOOR csv file by [this link](https://docs.google.com/spreadsheets/d/1J50qlpazz9-BZ9HpLJa7esmqiXov2bYRm--KeePo9i4/edit?gid=385102986#gid=385102986)

> [!WARNING]
> When you save this file into the hidden_files folder, you ALWAYS should name it `doors.csv`

Headers of the file:

1. **DOOR** - name of the door. You can use grid system or simple naming system
2. **IS_OPENED** - status of the door, is it opened or closed
3. **IS_UNLOCKED** - status of the door, is it locked or unlocked
4. **IS_VISIBLE** - does this door appear in `DOOR LIST` command. Invisible doors are still operatable 
5. **PASSWORD** - does this door requires password to operate with, all not `NONE` counts as password
6. **IS_BROKEN** - if not `NOMINAL` than door can't be opened, closed, locked or unlocked

> [!NOTE]
> Example of usage `item zone CARGO` or `item owner captain_name`

### DOOR LIST

Shows all the doors if they are visible. Doesn't show IS_BROKEN status (it might've come as surprise)

### DOOR STATUS

Shows full status of the select door, regardless of visibility

### DOOR OPEN {DOORNAME}

Opens door if not locked. Might require a password. Will not open a door if it's broken. If it is already opened - it will do nothing. If door succesfully opens telegram_integration will send a notification to the DM/GM

### DOOR CLOSE {DOORNAME}

Same as above, but about closing

### DOOR LOCK {DOORNAME}

Locks door if it was unlocked. Might require a password. Will not lock if it's broken. If already locked - it will do nothing. If door succesfully locks telegram_integration will send a notification to the DM/GM

### DOOR UNLOCK {DOORNAME}

Same as above, but about unlocking

## ALARM

Currently there's only one ALARM parameter at the moment: lockdown

ALARM LOCKDOWN locks and closes all the visible and unpassworded doors 

Sends notification to the DM/GM if integration is active

## SERVICE

This is mostly GM/DM tool, players can switch on/off some systems like light, gravity, AI and other. Works like doors, but more simple

Availible commands:

1. **SERVICE ON/ENABLE**
2. **SERVICE OFF/DISABLE**
3. **SERVICE STATUS**
4. **SERVICE LIST**

### SERVICE csv

You can access SERVICE csv file by [this link](https://docs.google.com/spreadsheets/d/1J50qlpazz9-BZ9HpLJa7esmqiXov2bYRm--KeePo9i4/edit?gid=1301457828#gid=1301457828)

> [!WARNING]
> When you save this file into the hidden_files folder, you ALWAYS should name it `service.csv`

Headers of the file:

1. **NAME** - Name of the service
2. **IS_ON** - Status of the service, is it enabled or disabled
3. **STATUS** - Is it functional/broken
4. **PASSWORD** - If not NONE, password will be required to turn service on/off

### SERVICE ON/ENABLE {SERVICE_NAME}

If service is turned off, this will turn service on. Might require password. Will send notification to the DM/GM

### SERVICE OFF/DISABLE {SERVICE_NAME}

Same as above, but turn off

### SERVICE STATUS {SERVICE_NAME}

Shows full information about one particular service (doesn't show password)

### SERVICE LIST

Shows full list of availible services

## SELFDESTRUCT

Complex command that activates or deactives selfdestruct command. In current version can be issued with two different command names and doesn't have csv config (yet)

Availible commands:

1. **SELFDESTRUCT TIMER**
2. **SELFDESTRUCT START/INITIATE**
3. **SELFDESTRUCT STOP/ABORT**
4. **SELFDESTRUCT STATUS**

And secret command SELFDESTRUCT PLEASEDIE if you just want immideate death screen. Not documented, can't recommend to show this command to the player

### SELFDESTRUCT TIMER

Changes self-destruct timer time. Default is 600, can be set to any amount

If set to negative, timer will trigger immidetaly 

### SELFDESTRUCT START/INITIATE

Might require password

Starts background timer

Every time player can input command there will be notification message about time left before selfdestruct trigger

### SELFDESTRUCT STOP/ABORT

Might require password

Starts background timer

Shows player his left time before selfdestruct trigger

### SELFDESTRUCT STATUS

Shows to the player next information:

1. TIMER seconds amount, how many seconds there will be before an explosion
2. Is password required to start the sequence
3. Is password required to stop the sequence
4. Current SELFDESTRUCT status, is TIMER is active

### SELFDESTRUCT EXPLODE

Not a typeable command, but this section describes what will happen if timer reaches 0

After timer reaches 0:

1. Terminal will say "Bye"
2. Wait 1 second
3. Clear the screen
4. Blocks player's input
5. Starts to spam █ character into the screen constantly

# Modding

After some time playing around there comes the question - how to mod this Terminal for your usage?

Simple first step is to change the content of open_data folder, but that's not everything that might want to be moddable

## configs

As it is not in the separate file, i tried to make it more comfortable for potential user to change most important variables in one place

Configs are stored in main.py from line 15 `# SETTINGS SECTION` up to line 44

```py
# SETTINGS SECTION
# Things to set up audio for terminal
pygame.mixer.init(buffer = 2048)
pygame.mixer.set_num_channels(20)
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.load("audio/mother.wav")
sound1 = pygame.mixer.Sound("audio/typewriter-key-even.wav")
sound1.set_volume(0.1)
enable_music = True
enable_typewriter = True

# Parameters for slow typer
slow_line_sleep = 0.15
slow_type_speed = 1000

# file password settings
decryption_is_slow = True
decryption_speed = 1000
decryption_wav_divider = 10000
decryption_speed_wav = 1000
decryption_lag = 10

# Self Destruct settings
selfdestruct_timer = 600
selfdestruct_password_start = "hackme12"
selfdestruct_password_stop = "hackme14"
selfdestruct_active = False
selfdestruct_dead = False

# sleep time before startup starts working
start_sleep_time = 5

# break line for terminal AND (!) diag file
breakline = "- - - - - - - - - - - - - - - - - - - - - - -\n"
```

What are the interesting lines here?

1. `pygame.mixer.music.set_volume(0.1)` - number in () is volume of the background sound
2. `sound1.set_volume(0.1)` - number in () is volume of the typewriter sound
3. `enable_music = True` - Write "False" if you want to turn background sound off
4. `enable_typewriter = True` - Write "False" if you want to turn typewriter sound off
5. `slow_line_sleep = 0.15` - pause between the lines in (s) when outputting text
6. `slow_type_speed = 1000` - speed of outputting symbols. Higher the number - higher the speed of the output
7. `decryption_is_slow = True` - Write "False" if you want to remove waiting on decryption when FILE READ requires a password
8. `decryption_speed = 1000` - Speed of the decryption when FILE READ requires a password
9. `decryption_wav_divider = 10000` - As WAV files are greatly bigger by the size, this number artifically decreases it's size for the "decryption". Bigger the number - smaller the decryption number
10. `decryption_speed_wav = 1000` - Separate speed of the decryption for .wav files when FILE READ requires a password
11. `decryption_lag = 10` - Randomness during the decryption, needs for "jumping" waiting number. The bigger the number - bigger the randomness, but it might be slightly faster in the overall decryption
12. `selfdestruct_timer = 600` - starting timer for the selfdestruct sequence, default is 600 seconds
13. `selfdestruct_password_start = "hackme12"` - what password need sto be used to start selfdestruct sequence. Use "" if you don't need password to start
14. `selfdestruct_password_stop = "hackme14"` - what password need sto be used to stop selfdestruct sequence. Use "" if you don't need password to stop
15. `selfdestruct_active = False` - If you want self destruct timer to be active right from the start, change this on "True"
16. `start_sleep_time = 5` - timer between launching of the Terminal and writing the hidden_files/startup.txt and waiting for the input. This time was needed to actually give the laptop to the player, so he won't miss any content
17. `breakline = "- - - - - - - - - - - - - - - - - - - - - - -\n"` - line that used to separate the blocks in commands and DIAG file

## Removing/Renaming commands

There is a block of lines around line 723 

Left side in the list is the name that players input, right one is a function that players call

If you want to rename function - rename left part in the ""

If you want to remove function - delete the line entirely

If you want to add new name for the function - copy-paste the line and rename left part

```py
# List of all available commands in the terminal. They're not showing in help
# Delete some commands if you don't want your players to use them
# Rename some commands at the left part of list if you want to
all_command_list = {
    "help": help,
    "diag": diag,
    "file": file,
    "clear": clear,
    "item": item,
    "ping": ping,
    "door": door,
    "alarm": alarm,
    "service": service,
    "selfdestruct": selfdestruct,
    "suicide": selfdestruct
}
```

> [!CAUTION]
> There are two things you need to remember editing this block:
>
> 1. Comma (,) should be at the end of each line except for the last one, or python Terminal won't launch any commands
> 2. Name of the left side (inside of "") should be unique. If it duplicates - Terminal won't launch any commands

## Changing hidden files

Except for absoultely random text in open_data folder, files in hidden_data folder are triggered by other functions or events. Some of them should be designed specifically in certain way

### startup

This is just .txt file that player sees on startup of the Terminal. If you need longer pauses between the lines, spam spacebar

### shipdiag

This file should be written in certain way, as described in [this section](#diag-file-format)

### files passwords

files_passwords.txt is the file that used by FILE command, when Terminal checks if the certain filename uses a password to open. Example of the file:

```
AJ_new_sleepzone.txt 12345678
DA_artifact.txt knowledge
GK_1_encounter.txt IseaU789
```

On the left side is the exact name of the file and on the right side is the passwords that player needs to use to unlock the file

> [!CAUTION]
> If you write spacebar after the password - it will be part of the password. Example `"password     "`

### csv files

To change .csv files i recommend use [this google sheet](https://docs.google.com/spreadsheets/d/1J50qlpazz9-BZ9HpLJa7esmqiXov2bYRm--KeePo9i4/edit?gid=1301457828#gid=1301457828), than download and export as csv pages you need with the content you need

Make sure, that files you download will be renamed into:

1. doors.csv
2. items.csv
3. service.csv

Or this files will not be read by the Terminal

## audio

Except for .wav files in the open_data folder, there are two files that used for the Terminal:

1. audio/mother.wav
2. audio/typewriter-key-even

First file is the background file with all the noise you can hear, second one is key sound for typing

There is no support for multiple sounds in the category yet

## Translation

There is no simple localization tool yet, so to translate content into your language you need to do next steps:

1. Change content of .txt or .csv files of hidden_data and open_data
2. Open main.py and change content of `output(f" translation here")` and `send_notification(f" translation here")`

There are about 140 lines of p.2 in the main.py, so translation might take some time

In the future there will be .csv file with every line loading into the Terminal, but not for now

# Known bugs

## DIAG breakline

If you add spacebar to the end of the breakline, so it will differ from the one in python config - diag command will break. If you want to change breakline in the shipdiag file, you need also change breakline in the config for an exact match

## Spacebar after param

If you write space

# Plans

This is not the final version, and potentially i will update Terminal as soon as there will be interest in this. But there are some nearest future plans:

## Localisation csv

To minimize user interference with the code (it's scary), first thing on the next massive update is localization sheet. 

It will consist from line ID, variable name, context of the text, text itself 

## Discord integration

This is the part i need help with, but as soon as someone will send (or i will find) - discord integration will also be implemented in the Terminal. Will work in the same way, as the Telegram integration

# Suggestions, Feedbacks and Patches

If you have any patches or bugfixes - please send them in the Issues on the github

The same goes with any expantion for the Terminal (adding Tetris, minigames, puzzles, e.t.c.)

The same goes with any localization or reformatting of the files (text files format, new startup, any flavoring)

If you want to suggest anything, feedback anything - feel free to contact me on any platform from the Contacts section or github

# Contacts

Ways you can contact me:

* (Telegram)[t.me/HalfDeady]
* Discord - HalfDeady (just add me)
* (email)[halfdeadanarchyst@gmail.com]
* And github

# Credits

[windows-terminal-shaders](https://github.com/Hammster/windows-terminal-shaders) for his exceptional visual base for this terminal. Without these cool graphics RP-retro-Terminal would be less atmospheric

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
