# -*- coding: utf-8 -*-

import streamlit as st
import numpy as np
import pandas as pd
import time
from matplotlib import pyplot as plt

import altair as alt
from vega_datasets import data
import webbrowser

def main():

    url = 'https://altair-viz.github.io/'

    if st.button('altair'):
        webbrowser.open_new_tab(url)

    source = data.cars()

    fig = alt.Chart(source).mark_circle(size=60).encode(
        x='Horsepower',
        y='Miles_per_Gallon',
        color='Origin',
        tooltip=['Name', 'Origin', 'Horsepower', 'Miles_per_Gallon']
    ).properties(
        width=500,
        height=500
    ).interactive()

    st.write(fig)

if __name__ == '__main__':
    main()
