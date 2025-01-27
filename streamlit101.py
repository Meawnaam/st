import streamlit as st
import pandas as pd
import numpy as pd
import altair as alt

st.title("Hello world")
# we must download conda environment 
placeholder = st.empty()
status = st.radio("Select an option",
                ["Error", "Success"], index = None)
                


if status == "Success" :
    placeholder.success("Success!")
else :
    placeholder.error("Error")


st.info("Hello, It is awesome!")
st.success("This is cool!")
st.error("This is an error massag.e")
st.warning("This is a warning")


st.header("Area chart")
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
st.area_chart(chart_data)


df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/refs/heads/master/penguins.csv")

c = alt.Chart(df).mark_circle(size=60).encode(
    x="bill_length_mm",
    y="body_mass_g",
    color="species",
).interactive()

st.altair_chart(c, use_container_width=True)
