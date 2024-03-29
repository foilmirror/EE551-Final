import wiiu_scraper

chars = [
    'mario',
    'donkeykong',
    'link',
    'samus',
    'dsamus',
    'yoshi',
    'kirby',
    'fox',
    'pikachu',
    'luigi',
    'ness',
    'falcon',
    'jigglypuff',
    'peach',
    'daisy',
    'bowser',
    'iceclimbers',
    'shiek',
    'zelda',
    'drmario',
    'pichu',
    'falco',
    'marth',
    'lucina',
    'younglink',
    'ganondorf',
    'mewtwo',
    'roy',
    'chrom',
    'gnw',
    'metaknight',
    'pit',
    'dpit',
    'zss',
    'wario',
    'snake',
    'ike',
    'squirtle',
    'ivysaur',
    'charizard',
    'diddykong',
    'lucas',
    'sonic',
    'dedede',
    'olimar',
    'lucario',
    'rob',
    'toonlink',
    'wolf',
    'villager',
    'megaman',
    'wiifit',
    'rosalina',
    'littlemac',
    'greninja',
    'brawler',
    'swordfighter',
    'gunner',
    'palutena',
    'pacman',
    'robin',
    'shulk',
    'bowserjr',
    'duckhunt',
    'ryu',
    'ken',
    'cloud',
    'corrin',
    'bayonetta',
    'inkling',
    'ridley',
    'simon',
    'richter',
    'krool',
    'isabelle',
    'incineroar',
    'plant',
    'joker',
    'hero',
    'banjo',
    'terry'
    ]

brawlchars = {
    'mario': 'Mario',
    'donkeykong': 'Donkey Kong',
    'link': 'Link',
    'samus': 'Samus',
    'yoshi': 'Yoshi',
    'kirby': 'Kirby',
    'fox': 'Fox',
    'pikachu': 'Pikachu',
    'luigi': 'Luigi',
    'ness': 'Ness',
    'falcon': 'Captain Falcon',
    'jigglypuff': 'Jigglypuff',
    'peach': 'Peach',
    'bowser': 'Bowser',
    'iceclimbers': 'Ice Climbers',
    'shiek': 'Shiek',
    'zelda': 'Zelda',
    'falco': 'Falco',
    'marth': 'Marth',
    'ganondorf': 'Ganondorf',
    'gnw': 'Mr. Game & Watch',
    'metaknight': 'Meta Knight',
    'pit': 'Pit',
    'zss': 'Zero Suit Samus',
    'wario': 'Wario',
    'snake': 'Snake',
    'ike': 'Ike',
    'squirtle': 'Squirtle',
    'ivysaur': 'Ivysaur',
    'charizard': 'Charizard',
    'diddykong': 'Diddy Kong',
    'lucas': 'Lucas',
    'sonic': 'Sonic',
    'dedede': 'King Dedede',
    'olimar': 'Olimar',
    'lucario': 'Lucario',
    'rob': 'R.O.B.',
    'toonlink': 'Toon Link',
    'wolf': 'Wolf',
    }

sm4shchars = {
    'mario': 'Mario',
    'donkeykong': 'Donkey%20Kong',
    'link': 'Link',
    'samus': 'Samus',
    'yoshi': 'Yoshi',
    'kirby': 'Kirby',
    'fox': 'Fox',
    'pikachu': 'Pikachu',
    'luigi': 'Luigi',
    'ness': 'Ness',
    'falcon': 'Captain%20Falcon',
    'jigglypuff': 'Jigglypuff',
    'peach': 'Peach',
    'bowser': 'Bowser',
    'shiek': 'Shiek',
    'zelda': 'Zelda',
    'drmario': 'Dr.%20Mario',
    'falco': 'Falco',
    'marth': 'Marth',
    'lucina': 'Lucina',
    'ganondorf': 'Ganondorf',
    'mewtwo': 'Mewtwo',
    'roy': 'Roy',
    'gnw': 'Game%20And%20Watch',
    'metaknight': 'Meta%20Knight',
    'pit': 'Pit',
    'dpit': 'Dark%20Pit',
    'zss': 'Zero%20Suit%20Samus',
    'wario': 'Wario',
    'ike': 'Ike',
    'charizard': 'Charizard',
    'diddykong': 'Diddy%20Kong',
    'lucas': 'Lucas',
    'sonic': 'Sonic',
    'dedede': 'King%20Dedede',
    'olimar': 'Olimar',
    'lucario': 'Lucario',
    'rob': 'R.O.B.',
    'toonlink': 'Toon%20Link',
    'villager': 'Villager',
    'megaman': 'Mega%20Man',
    'wiifit': 'Wii%20Fit%20Trainer',
    'rosalina': 'Rosalina%20And%20Luma',
    'littlemac': 'Little%20Mac',
    'greninja': 'Greninja',
    'brawler': None,
    'swordfighter': None,
    'gunner': None,
    'palutena': 'Palutena',
    'pacman': 'PAC-MAN',
    'robin': 'Robin',
    'shulk': 'Shulk',
    'bowserjr': 'Bowser%20Jr.',
    'duckhunt': 'Duck%20Hunt',
    'ryu': 'Ryu',
    'cloud': 'Cloud',
    'corrin': 'Corrin',
    'bayonetta': 'Bayonetta',
    }

ultimatechars = {
    'mario': 'Mario',
    'donkeykong': 'Donkey Kong',
    'link': 'Link',
    'samus': 'Samus',
    'dsamus': 'Dark Samus',
    'yoshi': 'Yoshi',
    'kirby': 'Kirby',
    'fox': 'Fox',
    'pikachu': 'Pikachu',
    'luigi': 'Luigi',
    'ness': 'Ness',
    'falcon': 'Captain Falcon',
    'jigglypuff': 'Jigglypuff',
    'peach': 'Peach',
    'daisy': 'Daisy',
    'bowser': 'Bowser',
    'iceclimbers': 'Ice Climbers',
    'shiek': 'Shiek',
    'zelda': 'Zelda',
    'drmario': 'Dr. Mario',
    'pichu': 'Pichu',
    'falco': 'Falco',
    'marth': 'Marth',
    'lucina': 'Lucina',
    'younglink': 'Young Link',
    'ganondorf': 'Ganondorf',
    'mewtwo': 'Mewtwo',
    'roy': 'Roy',
    'chrom': 'Chrom',
    'gnw': 'Mr. Game & Watch',
    'metaknight': 'Meta Knight',
    'pit': 'Pit',
    'dpit': 'Dark Pit',
    'zss': 'Zero Suit Samus',
    'wario': 'Wario',
    'snake': 'Snake',
    'ike': 'Ike',
    'squirtle': 'Squirtle',
    'ivysaur': 'Ivysaur',
    'charizard': 'Charizard',
    'diddykong': 'Diddy Kong',
    'lucas': 'Lucas',
    'sonic': 'Sonic',
    'dedede': 'King Dedede',
    'olimar': 'Olimar',
    'lucario': 'Lucario',
    'rob': 'R.O.B.',
    'toonlink': 'Toon Link',
    'wolf': 'Wolf',
    'villager': 'Villager',
    'megaman': 'Mega Man',
    'wiifit': 'Wii Fit Trainer',
    'rosalina': 'Rosalina & Luma',
    'littlemac': 'Little Mac',
    'greninja': 'Greninja',
    'brawler': 'Mii Brawler',
    'swordfighter': 'Mii Swordfighter',
    'gunner': 'Mii Gunner',
    'palutena': 'Palutena',
    'pacman': 'Pac-Man',
    'robin': 'Robin',
    'shulk': 'Shulk',
    'bowserjr': 'Bowser Jr.',
    'duckhunt': 'Duck Hunt',
    'ryu': 'Ryu',
    'ken': 'Ken',
    'cloud': 'Cloud',
    'corrin': 'Corrin',
    'bayonetta': 'Bayonetta',
    'inkling': 'Inkling',
    'ridley': 'Ridley',
    'simon': 'Simon',
    'richter': 'Richter',
    'krool': 'King K. Rool',
    'isabelle': 'Isabelle',
    'incineroar': 'Incineroar',
    'plant': 'Piranha Plant',
    'joker': 'Joker',
    'hero': 'Hero',
    'banjo': 'Banjo & Kazooie',
    'terry': 'Terry'
    }


attributes = [
    'weight', 'gravity', 'walkspeed', 'runspeed', 'initialdash', 'airspeed', 'airacceleration',
    'shtime', 'fhtime', 'fallspeed', 'ffspeed', 'jumpsquat'
    ]
groundmoves = [
    'jab', 'dashattack', 'ftilt', 'utilt', 'dtilt', 'fsmash', 'usmash', 'dsmash' 
    ]
grabs = [
    'standinggrab', 'dashgrab', 'pivotgrab' 
    ]
throws = [
    'fthrow', 'bthrow', 'uthrow', 'dthrow' 
    ]
aerialmoves = [
    'nair', 'fair', 'bair', 'dair' 
    ]
specialmoves = [
    'neutralb', 'sideb', 'upb', 'downb'
    ]

sm4shmoves = {
    'weight': 'Weight',
    'gravity': 'Gravity',
    'walkspeed': 'Walk Speed',
    'runspeed': 'Run Speed',
    'initialdash': None,
    'airspeed': 'Air Speed',
    'airacceleration': 'Air Acceleration',
    'shtime': 'SH Air Time',
    'fhtime': 'FH Air Time',
    'fallspeed': 'Fall Speed',
    'ffspeed': 'Fast Fall Speed',
    'jumpsquat': 'Jumpsquat',
    'jab': 'Jab',
    'dashattack': 'Dash Attack',
    'ftilt': 'Ftilt',
    'utilt': 'Utilt',
    'dtilt': 'Dtilt',
    'fsmash': 'Fsmash',
    'usmash': 'Usmash',
    'dsmash': 'Dsmash',
    'standinggrab': 'Standing Grab',
    'dashgrab': 'Dash Grab',
    'pivotgrab': 'Pivot Grab',
    'fthrow': 'Fthrow',
    'bthrow': 'Bthrow',
    'uthrow': 'Uthrow',
    'dthrow': 'Dthrow',
    'nair': 'Nair',
    'fair': 'Fair',
    'bair': 'Bair',
    'dair': 'Dair',
    'neutralb': None,
    'sideb': None,
    'upb': None,
    'downb': None
    }


def sort(char, move):
    if move.lower() in attributes:
        section = 0
    elif move.lower() in groundmoves:
        section = 1
    elif move.lower() in grabs:
        section = 2
    elif move.lower() in throws:
        section = 3
    elif move.lower() in aerialmoves:
        section = 4
    elif move.lower() in specialmoves:
        section = 5
    else:
        return('Unknown move')
    if char.lower() in sm4shchars.keys():
        return(wiiu_scraper.getData(sm4shchars[char], sm4shmoves[move], section))
    else:
        return('Unknown character')
    return('***Testing imports***')

