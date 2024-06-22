import streamlit as st
import pandas as pd
from utils import getModel 
from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification
from st_draggable_list import DraggableList as dList

tilt = "duane browns goal this season is to see how many qb injuries he can be responsible"

text = "\n\n:red[almost like a 40yr old lt is not a good idea especially if your qb is 40 too]"
st.set_page_config(layout="wide")

modelsfile = "models/hf_models.csv"

file = open(modelsfile)
numline = len(file.readlines()) - 1

st.title("Model testing")

st.markdown("**Test sentence:** " + tilt)

cols = st.columns(4 , gap="medium")

for row in range(1, numline):
    task, model_name, framework = getModel(row, modelsfile)
    if framework == "pt":
        pipe = pipeline(task, model=model_name)
    else:
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForSequenceClassification.from_pretrained(model_name, from_tf=True)    
        pipe = pipeline(task, model=model, tokenizer=tokenizer)
    col = cols[(row-1)%4]    
    tile = col.container(height = 250)

    tile.caption(str(row) + " " + model_name)
    df = pd.DataFrame(pipe(tilt, top_k = 3))
    tile.write(df)

# draglist = pd.read_csv("models/ordered_models.csv", sep=";")

# slist = dList(draglist.to_dict("records"))

# cols[4].write(slist)
