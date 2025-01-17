columns = [
    "trujący",                     # poisonous
    "kształt-kapelusza",           # cap-shape
    "powierzchnia-kapelusza",      # cap-surface
    "kolor-kapelusza",             # cap-color
    "siniaki",                     # bruises
    "zapach",                      # odor
    "przyczepność-blaszek",        # gill-attachment
    "rozstawienie-blaszek",        # gill-spacing
    "rozmiar-blaszek",             # gill-size
    "kolor-blaszek",               # gill-color
    "kształt-trzonu",              # stalk-shape
    "korzeń-trzonu",               # stalk-root
    "powierzchnia-trzonu-nad-pierścieniem", # stalk-surface-above-ring
    "powierzchnia-trzonu-pod-pierścieniem", # stalk-surface-below-ring
    "kolor-trzonu-nad-pierścieniem",       # stalk-color-above-ring
    "kolor-trzonu-pod-pierścieniem",       # stalk-color-below-ring
    "typ-osłony",                 # veil-type
    "kolor-osłony",               # veil-color
    "liczba-pierścieni",          # ring-number
    "typ-pierścienia",            # ring-type
    "kolor-wydruku-zarodników",   # spore-print-color
    "populacja",                  # population
    "siedlisko",                  # habitat
]

variable_data = [
    {'name': 'kształt-kapelusza', 'options': {
        'dzwonowaty': 'b',
        'stożkowaty': 'c',
        'wypukły': 'x',
        'płaski': 'f',
        'z guzkiem': 'k',
        'zagłębiony': 's'
    }},

    {'name': 'powierzchnia-kapelusza', 'options': {
        'włóknista': 'f',
        'rowkowana': 'g',
        'łuskowata': 'y',
        'gładka': 's'
    }},

    {'name': 'kolor-kapelusza', 'options': {
        'brązowy': 'n',
        'jasnobrązowy': 'b',
        'cynamonowy': 'c',
        'szary': 'g',
        'zielony': 'r',
        'różowy': 'p',
        'purpurowy': 'u',
        'czerwony': 'e',
        'biały': 'w',
        'żółty': 'y'
    }},

    {'name': 'siniaki', 'options': {
        'tak': 't',
        'nie': 'f'
    }},

    {'name': 'zapach', 'options': {
        'migdałowy': 'a',
        'anyżowy': 'l',
        'kreozotowy': 'c',
        'rybny': 'y',
        'nieprzyjemny': 'f',
        'stęchły': 'm',
        'żaden': 'n',
        'ostry': 'p',
        'korzenny': 's'
    }},

    {'name': 'przyczepność-blaszek', 'options': {
        "przyczepione": "a",
        "opadające": "d",
        "wolne": "f",
        "wycięte": "n"
    }},

    {'name': 'rozstawienie-blaszek', 'options': {
        "bliskie": "c",
        "stłoczone": "w",
        "odległe": "d"
    }},

    {'name': 'rozmiar-blaszek', 'options': {
        "szerokie": "b",
        "wąskie": "n"
    }},

    {'name': 'kolor-blaszek', 'options': {
        "czarny": "k",
        "brązowy": "n",
        "jasnobrązowy": "b",
        "czekoladowy": "h",
        "szary": "g",
        "zielony": "r",
        "pomarańczowy": "o",
        "różowy": "p",
        "purpurowy": "u",
        "czerwony": "e",
        "biały": "w",
        "żółty": "y"
    }},

    {'name': 'kształt-trzonu', 'options': {
        "powiększający się": "e",
        "zwężający się": "t"
    }},

    {'name': 'korzeń-trzonu', 'options': {
        "bulwiasty": "b",
        "maczugowaty": "c",
        "kubkowaty": "u",
        "równy": "e",
        "ryzomorfy": "z",
        "zakorzeniony": "r",
        "brak": "?"
    }},
    
    {'name': 'powierzchnia-trzonu-nad-pierścieniem', 'options': {
        "włóknista": "f",
        "łuskowata": "y",
        "jedwabista": "k",
        "gładka": "s"
    }},

    {'name': 'powierzchnia-trzonu-pod-pierścieniem', 'options': {
        "włóknista": "f",
        "łuskowata": "y",
        "jedwabista": "k",
        "gładka": "s"
    }},

    {'name': 'kolor-trzonu-nad-pierścieniem', 'options': {
        "brązowy": "n",
        "jasnobrązowy": "b",
        "cynamonowy": "c",
        "szary": "g",
        "pomarańczowy": "o",
        "różowy": "p",
        "czerwony": "e",
        "biały": "w",
        "żółty": "y"
    }},

    {'name': 'kolor-trzonu-pod-pierścieniem', 'options': {
        "brązowy": "n",
        "jasnobrązowy": "b",
        "cynamonowy": "c",
        "szary": "g",
        "pomarańczowy": "o",
        "różowy": "p",
        "czerwony": "e",
        "biały": "w",
        "żółty": "y"
    }},

    {'name': 'typ-osłony', 'options': {
        "częściowa": "p",
        "uniwersalna": "u"
    }},

    {'name': 'kolor-osłony', 'options': {
        "brązowy": "n",
        "pomarańczowy": "o",
        "biały": "w",
        "żółty": "y"
    }},

    {'name': 'liczba-pierścieni', 'options': {
        "brak": "n",
        "jeden": "o",
        "dwa": "t"
    }},

    {'name': 'typ-pierścienia', 'options': {
        "weloniasty": "c",
        "zanikający": "e",
        "rozszerzający się": "f",
        "duży": "l",
        "brak": "n",
        "zwisający": "p",
        "pochwiasty": "s",
        "strefowy": "z"
    }},

    {'name': 'kolor-wydruku-zarodników', 'options': {
        "czarny": "k",
        "brązowy": "n",
        "jasnobrązowy": "b",
        "czekoladowy": "h",
        "zielony": "r",
        "pomarańczowy": "o",
        "purpurowy": "u",
        "biały": "w",
        "żółty": "y"
    }},

    {'name': 'populacja', 'options': {
        "obfita": "a",
        "skupiona": "c",
        "liczna": "n",
        "rozproszona": "s",
        "kilka": "v",
        "pojedyncza": "y"
    }},

    {'name': 'siedlisko', 'options': {
        "trawy": "g",
        "liście": "l",
        "łąki": "m",
        "ścieżki": "p",
        "miejski": "u",
        "nieużytki": "w",
        "lasy": "d"
    }}
]

encoding = {
    "trujący": {
        "p": 0,
        "e": 1
    },
    "kształt-kapelusza": {
        "b": 0,
        "c": 1,
        "x": 2,
        "f": 3,
        "k": 4,
        "s": 5
    },
    "powierzchnia-kapelusza": {
        "f": 0,
        "g": 1,
        "y": 2,
        "s": 3
    },
    "kolor-kapelusza": {
        "n": 0,
        "b": 1,
        "c": 2,
        "g": 3,
        "r": 4,
        "p": 5,
        "u": 6,
        "e": 7,
        "w": 8,
        "y": 9
    },
    "siniaki": {
        "t": 0,
        "f": 1
    },
    "zapach": {
        "a": 0,
        "l": 1,
        "c": 2,
        "y": 3,
        "f": 4,
        "m": 5,
        "n": 6,
        "p": 7,
        "s": 8
    },
    "przyczepność-blaszek": {
        "a": 0,
        "d": 1,
        "f": 2,
        "n": 3
    },
    "rozstawienie-blaszek": {
        "c": 0,
        "w": 1,
        "d": 2
    },
    "rozmiar-blaszek": {
        "b": 0,
        "n": 1
    },
    "kolor-blaszek": {
        "k": 0,
        "n": 1,
        "b": 2,
        "h": 3,
        "g": 4,
        "r": 5,
        "o": 6,
        "p": 7,
        "u": 8,
        "e": 9,
        "w": 10,
        "y": 11
    },
    "kształt-trzonu": {
        "e": 0,
        "t": 1
    },
    "korzeń-trzonu": {
        "b": 0,
        "c": 1,
        "u": 2,
        "e": 3,
        "z": 4,
        "r": 5,
        "?": 6
    },
    "powierzchnia-trzonu-nad-pierścieniem": {
        "f": 0,
        "y": 1,
        "k": 2,
        "s": 3
    },
    "powierzchnia-trzonu-pod-pierścieniem": {
        "f": 0,
        "y": 1,
        "k": 2,
        "s": 3
    },
    "kolor-trzonu-nad-pierścieniem": {
        "n": 0,
        "b": 1,
        "c": 2,
        "g": 3,
        "o": 4,
        "p": 5,
        "e": 6,
        "w": 7,
        "y": 8
    },
    "kolor-trzonu-pod-pierścieniem": {
        "n": 0,
        "b": 1,
        "c": 2,
        "g": 3,
        "o": 4,
        "p": 5,
        "e": 6,
        "w": 7,
        "y": 8
    },
    "typ-osłony": {
        "p": 0,
        "u": 1
    },
    "kolor-osłony": {
        "n": 0,
        "o": 1,
        "w": 2,
        "y": 3
    },
    "liczba-pierścieni": {
        "n": 0,
        "o": 1,
        "t": 2
    },
    "typ-pierścienia": {
        "c": 0,
        "e": 1,
        "f": 2,
        "l": 3,
        "n": 4,
        "p": 5,
        "s": 6,
        "z": 7
    },
    "kolor-wydruku-zarodników": {
        "k": 0,
        "n": 1,
        "b": 2,
        "h": 3,
        "r": 4,
        "o": 5,
        "u": 6,
        "w": 7,
        "y": 8
    },
    "populacja": {
        "a": 0,
        "c": 1,
        "n": 2,
        "s": 3,
        "v": 4,
        "y": 5
    },
    "siedlisko": {
        "g": 0,
        "l": 1,
        "m": 2,
        "p": 3,
        "u": 4,
        "w": 5,
        "d": 6
    }
}

if __name__ == "__main__":
    print("VARIABLE_DATA")
    print(f"size: {len(variable_data)}")
    print(f"names: {[ variable['name'] for variable in variable_data]}")