from .base_colors import letter_to_color_number


def convert(txt_filename, bash_filename):
    code = "\e[48;5;{}m  \e[0m"  # colors code # noqa: W605
    final_output = ""
    with open(txt_filename) as f:
        char = f.read(1)
        while char:
            if char != '\n':
                char = code.format(letter_to_color_number[char])
            final_output += char
            char = f.read(1)

    with open(bash_filename, "w+") as d:
        d.write('echo -e "{}"'.format(final_output))
