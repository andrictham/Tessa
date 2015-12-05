import sys
import os

sys.path.append("../../text_parser")
import text_parser

li = [i for i in os.walk(os.getcwd())]

root = li[0]

for fi in root[2]:
    if fi[len(fi)-10:] == "output.txt":
        text_parser.tojsonfile(fi[:len(fi)-10]+"parsed", text_parser.get_orbiturary_info(fi))


