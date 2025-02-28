mapping = {
    'mww': 5,
    'mwc': 4,
    'mwb': 3,
    'mw': 2,
    'Mi': 1,
    'ms': 1,
    'mb': 1,
    'md': 1,
    'ml': 1
}
def map_function(column):
    for key, value in mapping.items():
        column = column.replace(key, str(value))
    return column.astype('int')

def drop_columns(df, columns):
    return df.drop(columns=columns)