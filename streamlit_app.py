import pandas as pd
import streamlit as st

from streamlit_ace import st_ace

from src.load_handlers import load_data
from src.comparisons import compare_all, compare_row_by_row

st.set_page_config(page_title='Synonym', page_icon=':ghost:', layout='wide', initial_sidebar_state='auto')

st.title(':ghost: Synonym')
st.subheader('Stop seeing ghosts, start seeing data!')

with st.expander('How to use Synonym'):
    st.markdown('''
    Synonym is a tool to help you compare datasets. It can help you identify differences between two datasets, and help you understand why those differences exist.
        
    ### How to use Synonym

    1. **Load Datasets**:
        - Upload two datasets you would like to compare.
        - You can upload datasets in CSV or Excel format.

    2. **Supply Read Options**
        - If your dataset requires special pandas read options, you can supply them in JSON format.
        - This is useful if your dataset has a non-standard delimiter, encoding, or other special requirements.

    3. **Compare Datasets**
        - Click the "Compare datasets" button to compare the two datasets.
        - Select the **Key** columns to compare the datasets by.
            - This could be a unique identifier, such as a:
                
                - `user_id`
                - `order_id`
                - `transaction_id`
                - `department_id`
            
                or maybe a combination of columns, such as:

                - `first_name` and `last_name`
                - `street_address` and `city`
                - `product_name` and `product_category`
                - `product_id` and `department_id`
            
                anything that uniquely identifies a row in the dataset.
            - Provide those columns, otherwise we'll look in the dataset order, row by row.
            - **It is Highly recommended to provide join columns**.
        - Synonym will compare the datasets column by column and row by row.
        - If there are any differences, Synonym will explain why they exist.

    4. **Interpret Results**
        - Synonym will show you the differences between the datasets, in a set of 12 different metrics.
        - If the datasets are identical, Synonym will let you know.
        - If the datasets are not identical, Synonym will explain why.

    5. **Export Results**
        - You can export the results of the comparison to a CSV file.
        - Hover over the top right corner of the comparison results and click the download button.

    If you encounter any issues, please let us know by opening an issue on our [GitHub repository](https://github.com/branden-ciranni/synonym).
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

    provide_join_on_cols = st.checkbox('Provide Key Columns to Join on?', key='join_on_cols_checkbox')
    if provide_join_on_cols:
        all_cols = set(df1.columns).union(set(df2.columns))
        join_cols = st.multiselect('Key Columns to Join on', list(all_cols), key='join_on_cols_multiselect')
    else:
        join_cols = None

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
                    st.write(f'#### {comparison["metric"]}')
                    cola, _, colb = st.columns([5,1,5])

                    try:
                        cola.dataframe(comparison['result1'], use_container_width=True)
                    except Exception:
                        cola.write(comparison['result1'])
                    
                    try:
                        colb.dataframe(comparison['result2'], use_container_width=True)
                    except Exception:
                        colb.write(comparison['result2'])

                    res = comparison['comparison']
                    if res:
                        st.write(f'Result: :white_check_mark: {res}')
                    else:
                        st.write(f'Result: :x: {res}')
                    st.write(comparison['explanation'])
                    st.write('---')

            st.subheader('Row by Row Comparison')
            comparsion = compare_row_by_row(df1, df2, join_cols=join_cols)
            st.dataframe(comparsion, use_container_width=True)
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