columns = [
    "poisonous",
    "cap-shape",
    "cap-surface",
    "cap-color",
    "bruises",
    "odor",
    "gill-attachment",
    "gill-spacing",
    "gill-size",
    "gill-color",
    "stalk-shape",
    "stalk-root",
    "stalk-surface-above-ring",
    "stalk-surface-below-ring",
    "stalk-color-above-ring",
    "stalk-color-below-ring",
    "veil-type",
    "veil-color",
    "ring-number",
    "ring-type",
    "spore-print-color",
    "population",
    "habitat",
]

variable_data = [
    {'name': 'cap-shape', 'options': {
        'bell': 'b',
        'conical': 'c',
        'convex': 'x',
        'flat': 'f',
        'knobbed': 'k',
        'sunken': 's'
    }},

    {'name': 'cap-surface', 'options': {
        'fibrous': 'f',
        'grooves': 'g',
        'scaly': 'y',
        'smooth': 's'
    }},

    {'name': 'cap-color', 'options': {
        "brown": 'n',
		"buff": 'b',
		"cinnamon": 'c',
		"gray": 'g',
		"green": 'r',
		"pink": 'p',
		"purple": 'u',
		"red": 'e',
		"white": 'w',
		"yellow": 'y'
    }},

    {'name': 'bruises', 'options': {
        'yes': 't',
        'no': 'f'
    }},

    {'name': 'odor', 'options': {
        'almond': 'a',
		'anise': 'l',
		'creosote': 'c',
		'fishy': 'y',
		'foul': 'f',
		'musty': 'm',
		'none': 'n',
		'pungent': 'p',
		'spicy': 's'
    }},

    {'name': 'gill-attachment', 'options': {
        "attached": "a",
		"descending": "d",
		"free": "f",
		"notched": "n"
    }},

    {'name': 'gill-spacing', 'options': {
        "close": "c",
		"crowded": "w",
		"distant": "d"
    }},

    {'name': 'gill-size', 'options': {
        "broad": "b",
		"narrow": "n"
    }},
    {'name': 'gill-color', 'options': {
        "black": "k",
		"brown": "n",
		"buff": "b",
		"chocolate": "h",
		"gray": "g",
        "green": "r",
		"orange": "o",
		"pink": "p",
		"purple": "u",
		"red": "e",
        "white": "w",
		"yellow": "y"
    }},
    {'name': 'stalk-shape', 'options': {
        "enlarging": "e",
		"tapering": "t"
    }},
    {'name': 'stalk-root', 'options': {
        "bulbous": "b",
		"club": "c",
		"cup": "u",
		"equal": "e",
		 "rhizomorphs": "z",
		"rooted": "r",
		"missing": "?"
    }},
		
    {'name': 'stalk-surface-above-ring', 'options': {
        "fibrous": "f",
		"scaly": "y",
		"silky": "k",
		"smooth": "s"
    }},
    {'name': 'stalk-surface-below-ring', 'options': {
        "fibrous": "f",
		"scaly": "y",
		"silky": "k",
		"smooth": "s"
    }},
    {'name': 'stalk-color-above-ring', 'options': {
        "brown": "n",
		"buff": "b",
		"cinnamon": "c",
		"gray": "g",
		"orange": "o",
		 "pink": "p",
		"red": "e",
		"white": "w",
		"yellow": "y"
    }},
    {'name': 'stalk-color-below-ring', 'options': {
        "brown": "n",
		"buff": "b",
		"cinnamon": "c",
		"gray": "g",
		"orange": "o",
		 "pink": "p",
		"red": "e",
		"white": "w",
		"yellow": "y"
    }},
    {'name': 'veil-type', 'options': {
        "partial": "p",
		"universal": "u"
    }},
    {'name': 'veil-color', 'options': {
        "brown": "n",
		"orange": "o",
		"white": "w",
		"yellow": "y"
    }},
    {'name': 'ring-number', 'options': {
        "none": "n",
		"one": "o",
		"two": "t"
    }},
    {'name': 'ring-type', 'options': {
        "cobwebby": "c",
		"evanescent": "e",
		"flaring": "f",
		"large": "l",
		"none": "n",
		"pendant": "p",
		"sheathing": "s",
		"zone": "z"
    }},
    {'name': 'spore-print-color', 'options': {
        "black": "k",
		"brown": "n",
		"buff": "b",
		"chocolate": "h",
		"green": "r",
		"orange": "o",
		"purple": "u",
		"white": "w",
		"yellow": "y"
    }},
    {'name': 'population', 'options': {
        "abundant": "a",
		"clustered": "c",
		"numerous": "n",
		"scattered": "s",
		"several": "v",
		"solitary": "y"
    }},
    {'name': 'habitat', 'options': {
        "grasses": "g",
		"leaves": "l",
		"meadows": "m",
		"paths": "p",
		"urban": "u",
		"waste": "w",
		"woods": "d"
    }},
]

encoding = {
    "poisonous": {
        "p": 0,
        "e": 1
    },
    "cap-shape": {
        "b": 0,
        "c": 1,
        "x": 2,
        "f": 3,
        "k": 4,
        "s": 5
    },
    "cap-surface": {
        "f": 0,
        "g": 1,
        "y": 2,
        "s": 3
    },
    "cap-color": {
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
    "bruises": {
        "t": 0,
        "f": 1
    },
    "odor": {
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
    "gill-attachment": {
        "a": 0,
        "d": 1,
        "f": 2,
        "n": 3
    },
    "gill-spacing": {
        "c": 0,
        "w": 1,
        "d": 2
    },
    "gill-size": {
        "b": 0,
        "n": 1
    },
    "gill-color": {
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
    "stalk-shape": {
        "e": 0,
        "t": 1
    },
    "stalk-root": {
        "b": 0,
        "c": 1,
        "u": 2,
        "e": 3,
        "z": 4,
        "r": 5,
        "?": 6
    },
    "stalk-surface-above-ring": {
        "f": 0,
        "y": 1,
        "k": 2,
        "s": 3
    },
    "stalk-surface-below-ring": {
        "f": 0,
        "y": 1,
        "k": 2,
        "s": 3
    },
    "stalk-color-above-ring": {
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
    "stalk-color-below-ring": {
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
    "veil-type": {
        "p": 0,
        "u": 1
    },
    "veil-color": {
        "n": 0,
        "o": 1,
        "w": 2,
        "y": 3
    },
    "ring-number": {
        "n": 0,
        "o": 1,
        "t": 2
    },
    "ring-type": {
        "c": 0,
        "e": 1,
        "f": 2,
        "l": 3,
        "n": 4,
        "p": 5,
        "s": 6,
        "z": 7
    },
    "spore-print-color": {
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
    "population": {
        "a": 0,
        "c": 1,
        "n": 2,
        "s": 3,
        "v": 4,
        "y": 5
    },
    "habitat": {
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