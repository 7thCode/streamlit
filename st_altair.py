# -*- coding: utf-8 -*-

import streamlit as st
import altair as alt
from vega_datasets import data
from matplotlib import pyplot as plt
import time

import webbrowser

def main():

    labels = ['G1', 'G2', 'G3', 'G4', 'G5']
    men_means = [20, 35, 30, 35, 27]
    women_means = [25, 32, 34, 20, 25]
    men_std = [2, 3, 4, 1, 2]
    women_std = [3, 5, 2, 3, 3]
    width = 0.35       # the width of the bars: can also be len(x) sequence

    fig, ax = plt.subplots()

    ax.bar(labels, men_means, width, yerr=men_std, label='Men')
    ax.bar(labels, women_means, width, yerr=women_std, bottom=men_means, label='Women')

    ax.set_ylabel('Scores')
    ax.set_title('Scores by group and gender')
    ax.legend()

    st.pyplot(fig)


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

    status_text = st.empty()
    # プログレスバー
    progress_bar = st.progress(0)

    for i in range(100):
        status_text.text(f'Progress: {i}%')
        # for ループ内でプログレスバーの状態を更新する
        progress_bar.progress(i + 1)
        time.sleep(0.1)

    status_text.text('Done!')
    st.balloons()

if __name__ == '__main__':
    main()
