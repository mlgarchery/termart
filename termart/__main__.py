import sys
import os
from PIL import Image
from .img_to_txt import paletteize, save_img_as_txt
from .base_colors import colors
from .txt_to_bash import convert


class ParamsException(Exception):
    pass


class MissingParameter(Exception):
    pass


if __name__ == "__main__":
    args = sys.argv[1:]
    try:
        if len(args) == 0:
            raise ParamsException

        if len(args) == 1:
            if args[0] == "-t":
                raise MissingParameter
            else:
                Image.open(args[0])

    except ParamsException:
        print("You must specify a parameter image_filepath or '-t'")
    except MissingParameter:
        print("Missing txt_filepath param")
    except IndexError:
        print("Image not Found")
    else:
        g_path = "generated/"
        txt_filename = "ddata.txt"
        bash_filename = "drawing.sh"
        if args[0] == "-t":
            print(
                "CONVERTING IT TO A BASH FILE ({}). Try 'bash drawing.sh'"
                .format(bash_filename)
            )
            convert(args[1], bash_filename)
        else:
            im = Image.open(args[0])
            # %% Convert the RGB image to only the color in the palette
            # this way we eliminate close color or non desirable ones
            p_im = paletteize(im.convert('RGB'), colors)
            p_im.save("{}result.png".format(g_path))
            # %%
            output = save_img_as_txt(p_im, txt_filename)
            print(
                "\nSAVING THE FOLLOWING to {} :\n{}"
                .format(txt_filename, output)
            )
            print("CONVERTING IT TO A BASH FILE ({})".format(bash_filename))
            convert(txt_filename, bash_filename)
            print("RUNNING 'bash drawing.sh'")
            os.system("bash drawing.sh")
