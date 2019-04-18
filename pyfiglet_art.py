import pyfiglet
from termcolor import colored


def print_art(msg, color):
    valid_colors = ("red", "green", "yellow", "blue",
                    "magenta", "cyan", "white")

    if color not in valid_colors:
        color = "cyan"

    art_msg = pyfiglet.figlet_format(msg)
    colored_art_msg = colored(art_msg, color=color)

    print(colored_art_msg)


msg = input("What would you like to print?")
color = input("What color?")
print_art(msg, color)
