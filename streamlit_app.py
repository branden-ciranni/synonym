import pandas as pd
import streamlit as st

from streamlit_ace import st_ace

from src.load_handlers import load_data
from src.comparisons import compare_all

st.set_page_config(page_title='Synonym', page_icon=':ghost:', layout='wide', initial_sidebar_state='auto')

st.title(':ghost: Synonym')
st.subheader('Stop seeing ghosts, start seeing data!')

st.markdown('''
:construction: **Under Construction** :construction:

This app is still in the works. We're working hard to let you compare datasets with ease. :hammer_and_wrench:
''')

st.markdown('---')
st.header('Load Datasets')

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

    # groupby_columns = st.checkbox('Group by columns?', key=f'groupby_columns__{key1}_{key2}')

    # if groupby_columns and df1 is not None and df2 is not None:
    #     col_left, _, col_right = st.columns([5,1,5])
    #     groupby_left = col_left.multiselect('Group by (Left Dataset)', df1.columns.tolist(), key=f'groupby_left__{key1}')
    #     groupby_right = col_right.multiselect('Group by (Right Dataset)', df2.columns.tolist(), key=f'groupby_right__{key2}')

    #     if groupby_left and groupby_right:
    #         df1 = df1.groupby(groupby_left)
    #         df2 = df2.groupby(groupby_right)

    #         print(df1.head())
    #         print(df2.head())

    #         col_left.write('Grouped Data')
    #         col_left.write(df1.head())

    #         col_right.write('Grouped Data')
    #         col_right.write(df2.head())

    if st.button('Compare datasets'):
        if df1 is not None and df2 is not None:
            all_comparisons = compare_all(df1=df1, df2=df2)

            final_res_container = st.container()

            num_comparisons = len(all_comparisons)
            num_matches = len([c for c in all_comparisons if c['comparison']])
            if num_matches == num_comparisons:
                final_res_container.success(f'All comparisons match! {num_matches}/{num_comparisons}')
            elif num_matches == 0:
                final_res_container.error(f'No comparisons match! {num_matches}/{num_comparisons}')
            else:
                final_res_container.warning(f'Some comparisons do not match! {num_matches}/{num_comparisons}')

            col3, _, col4 = st.columns([5,1,5])
            col3.subheader('Left Dataset')
            col4.subheader('Right Dataset')

            for comparison in all_comparisons:
                with st.container():
                    cola, _, colb = st.columns([5,1,5])

                    cola.write(f'**{comparison["metric"]}**')
                    cola.write(comparison['result1'])

                    colb.write(f'**{comparison["metric"]}**')
                    colb.write(comparison['result2'])

                    res = comparison['comparison']
                    if res:
                        st.write(f'Result: :white_check_mark: {res}')
                    else:
                        st.write(f'Result: :x: {res}')
                    st.write('---')

            st.subheader('Row by Row Comparison')
            comparsion = df1.compare(df2, result_names=('Left', 'Right'), align_axis=1)
            st.write(comparsion)
        else:
            st.error('Please load both datasets before comparing.')

col1, _, col2 = st.columns([5,1,5])

with col1:
    st.subheader('Left Dataset')
    load_file('left_dataset')

with col2:
    st.subheader('Right Dataset')
    load_file('right_dataset')

st.markdown('---')
st.header('Compare Datasets')


compare_datasets('left_dataset', 'right_dataset')