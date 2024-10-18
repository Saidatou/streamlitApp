import streamlit as st



st.write("Hello World")
st.title("Yoo Pi!!!! C'est le Weekend")

st.header("Part 1: Data Exploration")
st.write("In this section, we will explore the Altair cars dataset.")
st.markdown("*Further resources [here](https://altair-viz.github.io/gallery/selection_histogram.html)*")

slider = st.slider("Slider title", 0, 100, 50)
check = st.checkbox("Checkbox title", ["Add a constant", "Add beta 1", "Add beta 2"])
radio = st.radio("Radio title", ["Yes", "No"])
txt = st.text_input("Type here")
txt_area = st.text_area("Type here")
button = st.button("Button name")


if st.button("Click to launch"):
    button

st.snow()

st.balloons()