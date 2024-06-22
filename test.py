import string, utils
import contractions, pandas
# from utils import loadCSV2DF as csv
# from utils import getModel 
# from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification

text = "almost like a 40yr old lt is not a good idea especially if your qb is 40 too"

# text = contractions.fix(text)

# print(text)

# ans = text.translate(str.maketrans("","", string.punctuation))

# ans = " ".join(ans.split())

# print(ans)


# df = pandas.read_csv("models/ort_models.csv",  sep=";")

# print(df.loc[0,:]["model"])


# task, model1, framework = getModel(22, "models/hf_models.csv")

# #print(getModel(26))

# tokenizer = AutoTokenizer.from_pretrained("ZachBeesley/Tweet-Emotion")
# model = AutoModelForSequenceClassification.from_pretrained("ZachBeesley/Tweet-Emotion", from_tf = True)

# pipe = pipeline(task, model=model, tokenizer=tokenizer)
# #pipe = pipeline(task=task, model=model1)

# print(pipe(text, top_k = 3))
# # for row in csv("models/ort_models.csv"):
# #     print(row)

for i in range(0,25):
    print(i)
    