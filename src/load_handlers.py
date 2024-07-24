import pandas as pd
import io

from typing import Any, Dict, Optional

class UnsupportedFileFormat(Exception):
    pass

def load_data(
        file: Any,
        pandas_read_options: Optional[Dict[str, Any]] = None
    ) -> pd.DataFrame:
    """Load data from a file and return a DataFrame.

    :param file: A file uploaded by the user.
    :type file: io.BytesIO

    :return: A DataFrame containing the data from the file.
    :rtype: pd.DataFrame
    """
    if pandas_read_options is None:
        pandas_read_options = {}
    if file.name.endswith('csv'):
        data = pd.read_csv(file, **pandas_read_options)
    elif file.name.endswith('xlsx'):
        data = pd.read_excel(file, **pandas_read_options)
    else:
        raise UnsupportedFileFormat('Unsupported file format. Please upload a CSV or Excel file.')
    return data
    
    