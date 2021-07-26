import pandas as pd
from num2word.normalizer import number_converter
import os, sys

with open(os.path.join(sys.path[0], './INTERN_TEXTS/sents.txt'), "r") as file:
    examples = file.readlines()


for x in examples:
    print("TEXT", x)
    print("NUMBER CONVERTER", number_converter(x))
    predicted = number_converter(x)



df = pd.DataFrame(predicted, examples)

df.to_csv(index=True)

print(df)


