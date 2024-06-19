import string, utils
import contractions, pandas
from utils import loadCSV2DF as csv
from utils import getModel 
from transformers import pipeline

text = "almost like a 40yr old lt is not a good idea especially if your qb is 40 too"

# text = contractions.fix(text)

# print(text)

# ans = text.translate(str.maketrans("","", string.punctuation))

# ans = " ".join(ans.split())

# print(ans)


# df = pandas.read_csv("models/ort_models.csv",  sep=";")

# print(df.loc[0,:]["model"])


task, model1, file_name = getModel(26)

#print(getModel(26))

pipe = pipeline(task, model=model1)

print(pipe(text, top_k = 3))
# for row in csv("models/ort_models.csv"):
#     print(row)