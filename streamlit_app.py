import pandas as pd
import streamlit as st

from streamlit_ace import st_ace

from src.load_handlers import load_data

st.set_page_config(page_title='Synonym', page_icon=':ghost:', layout='wide', initial_sidebar_state='auto')

st.title(':ghost: Synonym')
st.subheader('Stop seeing ghosts, start seeing data!')

st.markdown('''
:construction: **Under Construction** :construction:

This app is still in the works. We're working hard to let you compare datasets with ease. :hammer_and_wrench:
''')

st.markdown('---')
st.subheader('Load Datasets')

@st.experimental_fragment
def load_file(key: str) -> None:
    file = st.file_uploader('Upload your dataset', type=['csv', 'xlsx'], key=f'file_uploader__{key}')
    supply_read_options = st.checkbox('Supply read options?', key=f'read_options_checkbox__{key}')
    if supply_read_options:
        read_options = st_ace(language='json', value='{}', height=100, theme='monokai', key=f'ace_editor__{key}')
        try:
            read_options = eval(read_options)
        except Exception as e:
            st.error(f'Error parsing read options: {e}')
    else:
        read_options = None
    if st.button('Load dataset', key=f'load_button__{key}'):
        df = load_data(file, read_options)
        st.write(df.head())
        st.session_state[f'df__{key}'] = df
        st.write(f':white_check_mark: Loaded {key}')
    else:
        st.write(f':x: Not Yet loaded {key}')

@st.experimental_fragment
def compare_datasets(key1: str, key2: str) -> None:
    df1 = st.session_state.get(f'df__{key1}')
    df2 = st.session_state.get(f'df__{key2}')
    if st.button('Compare datasets'):
        if df1 is not None and df2 is not None:
            comparsion = df1.compare(df2, result_names=('Left', 'Right'), align_axis=0)
            st.write(comparsion)
        else:
            st.error('Please load both datasets before comparing.')

col1, _, col2 = st.columns([4,1,4])

with col1:
    st.subheader('Left Dataset')
    load_file('left_dataset')

with col2:
    st.subheader('Right Dataset')
    load_file('right_dataset')

st.markdown('---')
st.subheader('Compare Datasets')

compare_datasets('left_dataset', 'right_dataset')