from __future__ import print_function
import sys, argparse, re

parser = argparse.ArgumentParser(description="The greatest CSS framework you have never used")
group = parser.add_mutually_exclusive_group()
group.add_argument("-m", help="Outputs minified CSS", action="store_true")
group.add_argument("-sass", help="Outputs Sass instead of normal CSS", action="store_true")
args = parser.parse_args()

reghex = re.compile(r"([0-9a-f])\1([0-9a-f])\2([0-9a-f])\3", re.I)

for number in range(16777215):
    hexcode = shorthex = hex(number)[2:].zfill(6)
    
    if args.m:
        m = reghex.match(hexcode)
        if m is not None:
            shorthex = m.string[0::2]
        print(
            ".color-" + hexcode + "{" +
            "color:#" + shorthex + ";" +
            "}", end = ""
        )
    elif args.sass:
        print(
            ".color-" + hexcode + "\n" +
            "    color: #" + hexcode
        )
    else:
        print(
            ".color-" + hexcode + " {\n" +
            "    color: #" + hexcode + ";\n" +
            "}"
        )