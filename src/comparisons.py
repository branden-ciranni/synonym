import pandas as pd

from typing import Any, Callable, Dict, List, Optional


def _compare(metric_name: str, metric_calc: Callable[[pd.DataFrame], Any], df1: pd.DataFrame, df2: pd.DataFrame) -> Dict[str, Any]:
    """Compare the metric between two DataFrames.

    :return: A dictionary containing the comparison results.
    :rtype: Dict[str, Any]
    """
    calc1 = metric_calc(df1)
    calc2 = metric_calc(df2)

    if isinstance(calc1, pd.Series):
        df1_cols = calc1.index.tolist()
        df2_cols = calc2.index.tolist()
        all_cols = list(set(df1_cols + df2_cols))
        
        explanation = ['**Explanation**']
        comparison = True

        for col in all_cols:
            val1 = calc1.get(col)
            val2 = calc2.get(col)
            if val1 is None:
                comparison = False
                explanation.append(f'- {col}: {val2} (only in right)')
            elif val2 is None:
                comparison = False
                explanation.append(f'- {col}: {val1} (only in left)')
            elif val1 != val2:
                comparison = False
                explanation.append(f'- {col}: {val1} (left) != {val2} (right)')
            else:
                explanation.append(f'- {col}: {val1} (left) == {val2} (right)')

        explanation = '\n'.join(explanation)
    else:
        comparison = calc1 == calc2
        explanation = f'**Explanation**\n- {calc1} (left) == {calc2} (right)' if comparison else f'**Explanation**\n- {calc1} (left) != {calc2} (right)'
    return {
        'metric': metric_name,
        'result1': calc1,
        'result2': calc2,
        'comparison': comparison,
        'explanation': explanation,
    }
    

def shapes(df1: pd.DataFrame, df2: pd.DataFrame) -> Dict[str, Any]:
    """Compare the shape of two DataFrames.
    
    :param df1: The first DataFrame.
    :type df1: pd.DataFrame
    
    :param df2: The second DataFrame.
    :type df2: pd.DataFrame
    
    :return: A dictionary containing the comparison results.
    :rtype: Dict[str, Any]
    """
    return _compare(
        metric_name='Shapes',
        metric_calc=lambda df: {'rows': df.shape[0], 'columns': df.shape[1]},
        df1=df1,
        df2=df2,
    )

def columns(df1: pd.DataFrame, df2: pd.DataFrame) -> Dict[str, Any]:
    """Compare the columns of two DataFrames.
    
    :param df1: The first DataFrame.
    :type df1: pd.DataFrame
    
    :param df2: The second DataFrame.
    :type df2: pd.DataFrame
    
    :return: A dictionary containing the comparison results.
    :rtype: Dict[str, Any]
    """
    return _compare(
        metric_name='Columns',
        metric_calc=lambda df: df.columns.tolist(),
        df1=df1,
        df2=df2,
    )

def dtypes(df1: pd.DataFrame, df2: pd.DataFrame) -> Dict[str, Any]:
    """Compare the data types of two DataFrames.
    
    :param df1: The first DataFrame.
    :type df1: pd.DataFrame
    
    :param df2: The second DataFrame.
    :type df2: pd.DataFrame
    
    :return: A dictionary containing the comparison results.
    :rtype: Dict[str, Any]
    """
    return _compare(
        metric_name='Data Types',
        metric_calc=lambda df: df.dtypes.rename('dtype').rename_axis('column'),
        df1=df1,
        df2=df2,
    )

def nulls(df1: pd.DataFrame, df2: pd.DataFrame) -> Dict[str, Any]:
    """Compare the null values of two DataFrames.
    
    :param df1: The first DataFrame.
    :type df1: pd.DataFrame
    
    :param df2: The second DataFrame.
    :type df2: pd.DataFrame
    
    :return: A dictionary containing the comparison results.
    :rtype: Dict[str, Any]
    """
    return _compare(
        metric_name='Nulls',
        metric_calc=lambda df: df.isnull().sum().rename('nulls').rename_axis('column'),
        df1=df1,
        df2=df2,
    )

def memory_usages(df1: pd.DataFrame, df2: pd.DataFrame) -> Dict[str, Any]:
    """Compare the memory usage of two DataFrames.
    
    :param df1: The first DataFrame.
    :type df1: pd.DataFrame
    
    :param df2: The second DataFrame.
    :type df2: pd.DataFrame
    
    :return: A dictionary containing the comparison results.
    :rtype: Dict[str, Any]
    """
    return _compare(
        metric_name='Memory Usage',
        metric_calc=lambda df: df.memory_usage(deep=True).sum(),
        df1=df1,
        df2=df2,
    )

def counts(df1: pd.DataFrame, df2: pd.DataFrame) -> Dict[str, Any]:
    """Compare the count of two DataFrames.
    
    :param df1: The first DataFrame.
    :type df1: pd.DataFrame
    
    :param df2: The second DataFrame.
    :type df2: pd.DataFrame
    
    :return: A dictionary containing the comparison results.
    :rtype: Dict[str, Any]
    """
    return _compare(
        metric_name='Count',
        metric_calc=lambda df: df.count().rename('count').rename_axis('column'),
        df1=df1,
        df2=df2,
    )

def unique_counts(df1: pd.DataFrame, df2: pd.DataFrame) -> Dict[str, Any]:
    """Compare the unique count of two DataFrames.
    
    :param df1: The first DataFrame.
    :type df1: pd.DataFrame
    
    :param df2: The second DataFrame.
    :type df2: pd.DataFrame
    
    :return: A dictionary containing the comparison results.
    :rtype: Dict[str, Any]
    """
    return _compare(
        metric_name='Unique Count',
        metric_calc=lambda df: df.nunique().rename('unique_count').rename_axis('column'),
        df1=df1,
        df2=df2,
    )

def means(df1: pd.DataFrame, df2: pd.DataFrame) -> Dict[str, Any]:
    """Compare the mean of two DataFrames.
    
    :param df1: The first DataFrame.
    :type df1: pd.DataFrame
    
    :param df2: The second DataFrame.
    :type df2: pd.DataFrame
    
    :return: A dictionary containing the comparison results.
    :rtype: Dict[str, Any]
    """
    return _compare(
        metric_name='Mean',
        metric_calc=lambda df: df.mean(numeric_only=True).rename('mean').rename_axis('column'),
        df1=df1,
        df2=df2,
    )

def medians(df1: pd.DataFrame, df2: pd.DataFrame) -> Dict[str, Any]:
    """Compare the median of two DataFrames.
    
    :param df1: The first DataFrame.
    :type df1: pd.DataFrame
    
    :param df2: The second DataFrame.
    :type df2: pd.DataFrame
    
    :return: A dictionary containing the comparison results.
    :rtype: Dict[str, Any]
    """
    return _compare(
        metric_name='Median',
        metric_calc=lambda df: df.median(numeric_only=True).rename('median').rename_axis('column'),
        df1=df1,
        df2=df2,
    )

def stds(df1: pd.DataFrame, df2: pd.DataFrame) -> Dict[str, Any]:
    """Compare the standard deviation of two DataFrames.
    
    :param df1: The first DataFrame.
    :type df1: pd.DataFrame
    
    :param df2: The second DataFrame.
    :type df2: pd.DataFrame
    
    :return: A dictionary containing the comparison results.
    :rtype: Dict[str, Any]
    """
    return _compare(
        metric_name='Standard Deviation',
        metric_calc=lambda df: df.std(numeric_only=True).rename('standard deviation').rename_axis('column'),
        df1=df1,
        df2=df2,
    )

def mins(df1: pd.DataFrame, df2: pd.DataFrame) -> Dict[str, Any]:
    """Compare the minimum value of two DataFrames.
    
    :param df1: The first DataFrame.
    :type df1: pd.DataFrame
    
    :param df2: The second DataFrame.
    :type df2: pd.DataFrame
    
    :return: A dictionary containing the comparison results.
    :rtype: Dict[str, Any]
    """
    return _compare(
        metric_name='Min',
        metric_calc=lambda df: df.min(numeric_only=True).rename('min').rename_axis('column'),
        df1=df1,
        df2=df2,
    )

def maxes(df1: pd.DataFrame, df2: pd.DataFrame) -> Dict[str, Any]:
    """Compare the maximum value of two DataFrames.
    
    :param df1: The first DataFrame.
    :type df1: pd.DataFrame
    
    :param df2: The second DataFrame.
    :type df2: pd.DataFrame
    
    :return: A dictionary containing the comparison results.
    :rtype: Dict[str, Any]
    """
    return _compare(
        metric_name='Max',
        metric_calc=lambda df: df.max(numeric_only=True).rename('max').rename_axis('column'),
        df1=df1,
        df2=df2,
    )    

def compare_all(df1: pd.DataFrame, df2: pd.DataFrame) -> List[Dict[str, Any]]:
    """Compare all the metrics between two DataFrames.
    
    :param df1: The first DataFrame.
    :type df1: pd.DataFrame
    
    :param df2: The second DataFrame.
    :type df2: pd.DataFrame
    
    :return: A list of dictionaries containing the comparison results.
    :rtype: List[Dict[str, Any]]
    """
    return [
        shapes(df1, df2),
        columns(df1, df2),
        dtypes(df1, df2),
        nulls(df1, df2),
        memory_usages(df1, df2),
        counts(df1, df2),
        unique_counts(df1, df2),
        means(df1, df2),
        medians(df1, df2),
        stds(df1, df2),
        mins(df1, df2),
        maxes(df1, df2),
    ]

def compare_row_by_row(df1: pd.DataFrame, df2: pd.DataFrame, join_cols: Optional[List[str]] = None) -> pd.DataFrame:
    """Compare two DataFrames row by row.

    Do a full outer join, and show, row by row, where there are differences column by column.
    Only the rows that are different will be shown.

    If the key is None, use the index.
    
    :param df1: The first DataFrame.
    :type df1: pd.DataFrame
    
    :param df2: The second DataFrame.
    :type df2: pd.DataFrame

    :param join_cols: The columns to join on.
    :type join_cols: List[str]
    
    :return: A DataFrame containing the comparison results.
    :rtype: pd.DataFrame
    """
    if join_cols is None:
        merged = pd.merge(
            df1, df2, left_index=True, right_index=True, how='outer', suffixes=('_left', '_right')
        )
    else:
        merged = pd.merge(
            df1, df2, on=join_cols, how='outer', suffixes=('_left', '_right')
        )

    join_cols = join_cols or []
    
    base_cols_1 = [col for col in df1.columns if col not in join_cols]
    base_cols_2 = [col for col in df2.columns if col not in join_cols]

    all_cols = list(set(base_cols_1 + base_cols_2))

    for col in all_cols:
        if col in join_cols:
            continue
        elif col in base_cols_1 and col in base_cols_2:
            merged[f'{col}_diff'] = merged[f'{col}_left'] != merged[f'{col}_right']
        elif col in base_cols_1:
            merged[f'{col}_diff'] = True
        elif col in base_cols_2:
            merged[f'{col}_diff'] = True
        else:
            raise ValueError(f'Column {col} not found in either DataFrame')
        
    # Sort ONLY the Diff Columns, leaving the original columns in the order they were
    original_cols = sorted([col for col in merged.columns if '_diff' not in col])
    diff_cols = sorted([col for col in merged.columns if '_diff' in col])

    merged = merged.reindex(columns=original_cols + diff_cols)

    return merged[merged[[f'{col}_diff' for col in all_cols]].any(axis=1) == True]
