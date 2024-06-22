import streamlit as st
from st_draggable_list import DraggableList as dList
import pandas as pd


col1, col2 = st.columns(2, gap = "medium")

with col1:
    draglist = pd.read_csv("models/ordered_models.csv", sep=";")
    slist = dList(draglist.to_dict("records"))
with col2:
    st.write(pd.DataFrame(slist))




