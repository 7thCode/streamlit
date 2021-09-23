# -*- coding: utf-8 -*-

import streamlit as st

import pandas as pd

def main():

    st.table(pd.DataFrame({
        'first column': [1, 2, 3, 4],
        'second column': [12, 20, 30, 40]
    }))

if __name__ == '__main__':
    main()
