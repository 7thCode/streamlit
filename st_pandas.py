# -*- coding: utf-8 -*-

import streamlit as st
import numpy as np
import pandas as pd
import time
from matplotlib import pyplot as plt

def main():

    st.table(pd.DataFrame({
        'first column': [1, 2, 3, 4],
        'second column': [12, 20, 30, 40]
    }))

if __name__ == '__main__':
    main()
