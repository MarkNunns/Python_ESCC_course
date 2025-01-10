# For module 2 session 8, Will's published code on Github came in 2 files, this is the 2nd file.
# Will had called his 2nd file:    "session_1_making_it_an_app.py"
# We need to use an appfile (.py) instead of a .ipynb file

# Module 2 Sessions 8 & 9 are about app building, similar to Module 1 Sessions 9 & 10.
# see MN's notes on MN's PC in here: D:\Mark\work\04 ESCC\a training\2024 Python\Course 1\Sessions 09 and 10\
# this includes walk-through for getting StreamLit working (in file:  Session 9 MN notes.docx)
# and further Steamlit trouble-shooting (in file: Streamlit preview problems.docx)

# These session notes (code) from Will may also provide answers if some Python functionality provided in Teams does not work...
# session_1_data_wrangling.py
# https://github.com/data-to-insight/ERN-sessions/blob/main/No%20Local%20Python/session_1_data_wrangling.py
# session_1_making_it_an_app.py
# https://github.com/data-to-insight/ERN-sessions/blob/main/No%20Local%20Python/session_1_making_it_an_app.py


# note that for this app file you need a requirements.txt file containing plotly

# This app works OK
# as always with an app.py file, you have to 'run the Python file' before you launch Streamlit Preview.
# when you Launch Streamlit Preview, you have to select several files.
# the app effectively runs a query to joing the files into 1 output file, that you can download.
# the app tidies the data too perhaps.

import streamlit as st

import pandas as pd

st.title('Benchmarking data pipeline')

# We can use
files = st.file_uploader('Please upload benchmarking data', 
                         accept_multiple_files=True)

# Set up an empty dictionary to store our dataframes in


if files:
    dfs = {}

    for f in files:

        df = pd.read_csv(f)

        # When files are uploaded in streamlit, they have a .name 
        # property, which can be used like the filepath one from glob
        list_name = f.name.split("/")[-1][:-17]#.split("_")[0]

        dfs[list_name] = df


    dfs = {key:dfs[key] for key in sorted(dfs.keys())}

    left_df = dfs['b1_children_in_need']

    permenant_columns = list(left_df.columns[:10])


    left_df = left_df.set_axis([f'b1_children_in_need_{column}' if (not column in permenant_columns) else column for column in left_df.columns], axis=1)


    for key, df in dfs.items():
        if ('headline_figures' not in key) & (key[:1] != 'b1') & ('mid-year' not in key) & (key[0] != 'a'):

            df = df.set_axis([f'{key}_{column}' if (not column in permenant_columns) else column for column in df.columns], axis=1)

            left_df = left_df.merge(df, how='left', on=permenant_columns)


    # st.write(left_df.columns)
    # st.dataframe(left_df)

    def convert_df(df):
        # IMPORTANT: Cache the conversion to prevent computation on every rerun
        return df.to_csv().encode("utf-8")

    csv = convert_df(left_df)

    st.download_button('Click to download wrangled data', csv, file_name='benchmarking.csv', mime="text/csv")