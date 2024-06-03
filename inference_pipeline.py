#from model import onnx_classifier
from methods import loadCSV2DF, convertDF
from model import getClassifier
import csv, pandas

comments = loadCSV2DF("Jets/week2.csv")

# for row in comments[:5]:
#      print(row)

classifier = getClassifier()

batch = comments.iloc[:, 0]
print(batch)

for row in batch[:50]:
    print(classifier(row))
# output = [classifier(x) for x in comments.iloc[:2]]
# print(output)