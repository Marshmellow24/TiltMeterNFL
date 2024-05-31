#from model import onnx_classifier
from methods import loadCSV
import csv

comments = loadCSV("Jets/week2.csv")

for row in comments:
    print(row)

