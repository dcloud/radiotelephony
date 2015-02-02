from itertools import cycle
from random import shuffle
import click

NATO_DICT = {
    "A": "Alpha",
    "B": "Bravo",
    "C": "Charlie",
    "D": "Delta",
    "E": "Echo",
    "F": "Foxtrot",
    "G": "Golf",
    "H": "Hotel",
    "I": "India",
    "J": "Juliet",
    "K": "Kilo",
    "L": "Lima",
    "M": "Mike",
    "N": "November",
    "O": "Oscar",
    "P": "Papa",
    "Q": "Quebec",
    "R": "Romeo",
    "S": "Sierra",
    "T": "Tango",
    "U": "Uniform",
    "V": "Victor",
    "W": "Whiskey",
    "X": "Xray",
    "Y": "Yankee",
    "Z": "Zulu",
    0: "Zero",
    1: "One",
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five",
    6: "Six",
    7: "Seven",
    8: "Eight",
    9: "Niner"
}

COLORS = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan']


@click.command()
@click.argument('input_words', nargs=-1)
@click.option('--compact/--no-compact', default=False)
def main(input_words, compact):
    shuffle(COLORS)
    color_cycle = cycle(COLORS)
    if not input_words:
        input_str = click.prompt("Enter a word or sentence to translate to callsigns", type=click.STRING)
        input_words = input_str.split(' ')
    for word in input_words:
        color = next(color_cycle)
        for letter in word:
            l = letter.upper()
            try:
                l = int(letter)
            except ValueError:
                pass
            nato_out = NATO_DICT.get(l, l)
            click.secho(nato_out[0], fg=color, bold=True, nl=False)
            click.secho(nato_out[1:], fg=color, nl=(not compact))
            if compact:
                click.echo(" ", nl=False)
        click.echo(" ")
