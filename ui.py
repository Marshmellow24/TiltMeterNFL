import streamlit as st
import pandas as pd
from utils import getModel 
from transformers import pipeline

text = "\n\n:red[almost like a 40yr old lt is not a good idea especially if your qb is 40 too]"


modelfile = "models/hf_models.csv"

file = open(modelfile)
numline = len(file.readlines()) - 1

st.title("Model testing")

st.markdown("**Test sentence:** " + text )

for row in range(1, numline):
    task, model1, file_name = getModel(row, modelfile)
    pipe = pipeline(task, model=model1)
    st.write(model1)
    df = pd.DataFrame(pipe(text, top_k = 3))
    st.write(df)