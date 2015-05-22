import os
import sys

for file in os.listdir("../poems"):
    if file.endswith("tsv"):
        identifier=file.replace(".poe.tsv","")
        for line in open("../poems/" + file):
            line = line.rstrip("\n")
            print identifier + "\t" + line

