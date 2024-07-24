import pandas as pd

def compare_dataframes(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    """Compare two DataFrames and return the differences.

    :param df1: The first DataFrame.
    :type df1: pd.DataFrame

    :param df2: The second DataFrame.
    :type df2: pd.DataFrame

    :return: A DataFrame containing the differences between the two DataFrames.
    :rtype: pd.DataFrame
    """
    comparison = df1.compare(df2)
    return comparison