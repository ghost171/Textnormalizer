from num2word.normalizer import number_converter
import os, sys

with open(os.path.join(sys.path[0], 'example.txt'), "r") as file:
    examples = file.readlines()


for x in examples:
    print("TEXT", x)
    print("NUMBER CONVERTER", number_converter(x))

