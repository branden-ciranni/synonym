import pandas as pd

from typing import Any, Callable, Dict, List


def _compare(metric_name: str, metric_calc: Callable[[pd.DataFrame], Any], df1: pd.DataFrame, df2: pd.DataFrame) -> Dict[str, Any]:
    """Compare the metric between two DataFrames.

    :return: A dictionary containing the comparison results.
    :rtype: Dict[str, Any]
    """
    calc1 = metric_calc(df1)
    calc2 = metric_calc(df2)

    if isinstance(calc1, pd.Series):
        comparison = calc1.equals(calc2)
    else:
        comparison = calc1 == calc2
    return {
        'metric': metric_name,
        'result1': calc1,
        'result2': calc2,
        'comparison': comparison,
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
        metric_name='shape',
        metric_calc=lambda df: f'{df.shape[0]} rows, {df.shape[1]} columns',
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
        metric_name='columns',
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
        metric_name='dtypes',
        metric_calc=lambda df: df.dtypes,
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
        metric_name='nulls',
        metric_calc=lambda df: df.isnull().sum(),
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
        metric_name='memory_usage',
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
        metric_name='count',
        metric_calc=lambda df: df.count(),
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
        metric_name='unique_count',
        metric_calc=lambda df: df.nunique(),
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
        metric_name='mean',
        metric_calc=lambda df: df.mean(numeric_only=True),
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
        metric_name='median',
        metric_calc=lambda df: df.median(numeric_only=True),
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
        metric_name='std',
        metric_calc=lambda df: df.std(numeric_only=True),
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
        metric_name='min',
        metric_calc=lambda df: df.min(numeric_only=True),
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
        metric_name='max',
        metric_calc=lambda df: df.max(numeric_only=True),
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


