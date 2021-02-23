# termart

Converting  very small images (or text) to terminal art (bash file that echo colors), like so: 

![](console.PNG)

from file `example_data/first_licorn.txt`, first line :
```
dddwwwwwwwdwww
ddwwdddddwwwddwdddddddddddbwr
dwwdbbbbbdwdjdwdddddddddddbwr
wwdbbdddbbdjjdw
wdbbbdwwdddjdww
wdbbvdwdwwwddw
wdbvvvdwwdwwdwdddddddddddgdgdg
wdbvvdwwdddwdwwddddddddddgdgdd
wdvvvdwwwwdwwdwwwwwddddddgggdg
```
## 8 standard ANSI colors https://en.wikipedia.org/wiki/ANSI_escape_code#Colors

First focus on the default linux terminal capabilities (targeting Ubuntu).

### Installation and usage 

Do `poetry install` then
```
python -m termart licorn.png
```

this will create a ddata.txt containing txt pixels, as mapped in file termart/base_colors.py :
```
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
```
It will also populate drawing.sh and show you what executing it looks like in the console

### More
```
python -m termart -t example_data/first_licorn.txt
```
will convert ddata.txt pixels to drawing.sh (useful if you need to do adjustments with your text editor and don't have a GUI for producing a licorn.png)