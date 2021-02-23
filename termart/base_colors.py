# 8 colors definitions
# ubuntu default terminal color, and one letter shorthand
colors = [
    ["black", "d", (0, 0, 0)],
    ["red", "r", (221, 0, 203)],
    ["green", "g", (10, 159, 0)],
    ["yellow", "y", (185, 167, 26)],
    ["blue", "b", (0, 23, 120)],
    ["magenta", "m", (94, 8, 131)],
    ["cyan", "c", (0, 140, 242)],
    ["white", "w", (241, 241, 241)]
]


def get_colors_rgb(colors):
    return [el[2] for el in colors]


color_to_letter = {
    el[2]: el[1] for el in colors
}
# palette contains R ints contiguously followed by G ints and R ints
palette = []
for i in range(3):
    channel = []
    for color in colors:
        channel.append(color[2][i])
    palette.extend(channel)
