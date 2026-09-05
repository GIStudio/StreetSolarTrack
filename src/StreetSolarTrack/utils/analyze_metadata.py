import pandas as pd

def analysis_meta(df):
    """
    Analyze the given DataFrame and return statistics for each column.

    Args:
        df (pd.DataFrame): The DataFrame to analyze.

    Returns:
        pd.DataFrame: A DataFrame containing the maximum, minimum, median, and mode for each column.
    """
    analysis_df = pd.DataFrame({
        'Max': df.max(),
        'Min': df.min(),
        'Median': df.median(),
        'Mode': df.mode().iloc[0]  # Get the first mode for each column
    })
    
    return analysis_df
