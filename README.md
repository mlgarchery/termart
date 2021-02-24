# termart

Converting  very small images (or text) to terminal art (bash file that echo colors), like so: 

![](console_output.png)

generated from file `example_data/first_licorn.txt` :
```
dddwwwwwwwdwww
ddwwdddddwwwddwdddddddddddbwr
dwwdbbbbbdwdydwdddddddddddbwr
wwdbbdddbbdyydw
wdbbbdwwdddydww
wdbbmdwdwwwddw
wdbmmmdwwdwwdwdddddddddddgdgdg
wdbmmdwwdddwdwwddddddddddgdgdd
wdmmmdwwwwdwwdwwwwwddddddgggdg
wdmmrdwwwwwwwdwwdddwwddddgdgdg
wwdrrdwwdddddwwdbbbdwddddgdgdg
dwdrrdwwwdwwwwdbmmbdw
dwwdrdwwwwdddddmmmmdw
ddwwddwwwwwwwwwdrrmdww
dddwwdwwwwwwwwwwddrrdw
ddddwdwwwwwwwwwwdwdrdw
ddddwdwwddddddwwdwwddw
ddddwdwwdwwwwdwwdwwwww
ddddwdwwdwddwdwwdw
ddddwdccdwddwdccdw
ddddwddddwddwddddw
ddddwwwwwwddwwwwww
```
## 8 standard ANSI colors https://en.wikipedia.org/wiki/ANSI_escape_code#Colors

First focus on the default linux terminal capabilities (targeting Ubuntu).

### Installation and usage 

For development

Do `poetry install`, `poetry shell`.

or you can install the package (to download from this repo):
```
pip install termart-0.1.0-py3-none-any.whl
# or
poetry add ./termart-0.1.0-py3-none-any.whl
# or
pipenv install termart-0.1.0-py3-none-any.whl
```

Then:
```
python -m termart licorn.png
```

this will create a ddata.txt containing textual pixels (r g y b m c w d), as mapped in file termart/base_colors.py :
```
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
```
It will also populate `drawing.sh` and show you what executing it looks like in the console:

![](console_output2.PNG)

### More
```
python -m termart -t example_data/first_licorn.txt
```
will convert ddata.txt pixels to drawing.sh (useful if you need to do adjustments with your text editor and don't have a GUI for producing a licorn.png)
