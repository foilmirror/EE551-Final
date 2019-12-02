# EE551-Final

My project is to create a Discord (https://discordapp.com/developers/docs/intro) bot that compares data from the two most recent Super Smash Bros video games.  Many Stevens students play these games competitively, and the bot would be able to provide quick information to them if used in the community's Discord server.  

It will take inputs for character and action, then provide data for that combination from each game that the character appears in.  The data will be downloaded from different websites by reading the pages' HTML sources.  This will require python basics (loops, if statements, dictionaries, etc), the Discord API, and likely an imported Python library (to help with web scraping).



# Results

In its current state, the bot is able to get data for each character in Super Smash Bros. for the Nintendo Wii U.

The best way to test this project is through Discord itself.  To use the bot, you will need a Discord account and server, and access to your the respective token and guild ID.  A file will need to be created, titled ".env".  The contents should be as follows:
```
# .env
DISCORD_TOKEN=(your user token)
DISCORD_GUILD=(your server's ID)
```
This file is not included here for security reasons, as sharing that information would allow others to use your account.  A list of moves that can be used for testing can be found here: http://kuroganehammer.com/Smash4/Pikachu, and any character from the game should work.  Some abbreviations are used for characters to simplify commands, such as "drmario" for Dr. Mario, or "zss" for Zero Suit Samus.

The bot's main loop is controlled by bot.py and the Discord library.  When the user inputs `>info mario jab`, the info command is run, and sorter.py is called.  Sorter.py contains dictionaries of characters and attacks that determine how the request should be handled.  Mario and Jab are found within the dictionaries, and passed to wiiu_scraper.py.  There, the BeautifulSoup library is used to collect HTML information from kuroganehammer.com.  BeautifulSoup turns the HTML file into a list of strings, which can then be sorted and searched through.  The data is then formatted and returned back to bot.py, where it is sent as a message in Discord.

Lists of characters and moves that can be used:

chars = [
    'mario',
    'donkeykong',
    'link',
    'samus',
    'yoshi',
    'kirby',
    'fox',
    'pikachu',
    'luigi',
    'ness',
    'falcon',
    'jigglypuff',
    'peach',
    'bowser',
    'shiek',
    'zelda',
    'drmario',
    'falco',
    'marth',
    'lucina',
    'ganondorf',
    'mewtwo',
    'roy',
    'gnw',
    'metaknight',
    'pit',
    'dpit',
    'zss',
    'wario',
    'ike',
    'charizard',
    'diddykong',
    'lucas',
    'sonic',
    'dedede',
    'olimar',
    'lucario',
    'rob',
    'toonlink',
    'villager',
    'megaman',
    'wiifit',
    'rosalina',
    'littlemac',
    'greninja',
    'palutena',
    'pacman',
    'robin',
    'shulk',
    'bowserjr',
    'duckhunt',
    'ryu',
    'cloud',
    'corrin',
    'bayonetta',
    ]
    
moves = [
    'jab', 'dashattack', 'ftilt', 'utilt', 'dtilt', 'fsmash', 'usmash', 'dsmash', 
    'standinggrab', 'dashgrab', 'pivotgrab', 
    'fthrow', 'bthrow', 'uthrow', 'dthrow', 
    'nair', 'fair', 'bair', 'dair' 
    ]
