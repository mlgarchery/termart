# Different convenient color data structures for our usage

# 8 colors definitions
# ubuntu default terminal color, and linux colors number
colors = [
    ["red",     "r",    (221, 0, 203),      1],
    ["green",   "g",    (10, 159, 0),       2],
    ["yellow",  "y",    (185, 167, 26),     3],
    ["blue",    "b",    (0, 23, 120),       4],
    ["magenta", "m",    (94, 8, 131),       5],
    ["cyan",    "c",    (0, 140, 242),      6],
    ["white",   "w",    (241, 241, 241),    15],
    ["black",   "d",    (0, 0, 0),          256],
]

color_to_letter = {el[2]: el[1] for el in colors}

letter_to_color_number = {el[1]: el[3] for el in colors}