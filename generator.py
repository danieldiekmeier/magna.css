from __future__ import print_function
import sys

if "-m" in sys.argv:
    output = 'minified'
elif "-sass" in sys.argv:
    output = 'sass'
else:
    output = 'normal'

for number in range(16777215):
    hexcode = hex(number)[2:].zfill(6)

    if output == 'minified':
        print(
            ".color-" + hexcode + " {" +
            "    color: #" + hexcode + ";" +
            "}"
        )
    elif output == 'sass':
        print(
            ".color-" + hexcode + "\n" +
            "    color: #" + hexcode + ""
        )
    else:
        print(
            ".color-" + hexcode + " {\n" +
            "    color: #" + hexcode + ";\n" +
            "}"
        )
