from .base_colors import color_to_letter


def distance(rgb1, rgb2):
    return sum([(rgb1[i]-rgb2[i])**2 for i in range(3)])


def nearest(rgb, colors):
    colors_rgb = [el[2] for el in colors]
    distances = [distance(rgb, rgb2) for rgb2 in colors_rgb]
    for i in range(len(distances)):
        if distances[i] == min(distances):
            return colors[i][2]
    raise BaseException("No nearest Element found")


def print_all_pixels(img):
    l, h = img.size
    result = []
    for x in range(l):
        for y in range(h):
            result.append(img.getpixel((x, y)))


def paletteize(img, colors):
    pixels = img.load()
    l, h = img.size
    for i in range(l):
        for j in range(h):
            pixels[i, j] = nearest(pixels[i, j], colors)
    return img


def save_img_as_txt(img, fp):
    output = ""
    x, y = img.size
    for j in range(y):
        for i in range(x):
            output += color_to_letter[img.getpixel((i, j))]
            if i == x-1:
                output += "\n"
    with open(fp, "w+") as f:
        f.write(output)
    return output


def get_unique_colors(img):
    return set(img.getcolors())
