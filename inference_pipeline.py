#from model import onnx_classifier
from utils import loadCSV2DF, convertDF
from model import getClassifier
import csv, pandas

comments = loadCSV2DF("Jets/week2.csv")

classifier = getClassifier()

batch = comments.iloc[:, 0]
print(batch)

for row in batch[:100]:
    print(row)
    print(classifier(row))
# output = [classifier(x) for x in comments.iloc[:2]]
# print(output)