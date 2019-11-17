import pandas as pd


def get_col_unique_val(df):
    """
    Extracts the unique values per column in df and returns them as dict.
    This also takes care of the cases where multiple values are stored as ; seperated strings.
    key:column name, value:list of unique values.
    """
    unique_vals = {}
    for col in df.columns:
        uq_vals = df[col].unique()
        # convert all to string
        uq_vals = [str(x) for x in uq_vals]

        split_semicol = [x.split(';') for x in uq_vals]
        uq_vals = {item.strip() for sublist in split_semicol for item in sublist}

        unique_vals[col] = uq_vals

    return unique_vals


def get_na_summary(df, axis=0):
    """
    Gets the summary of the df by columns or rows.
    """
    na_summary = pd.DataFrame(df.isna().sum(axis=axis), columns=['na_count'])
    if axis == 0:
        na_summary.index.names = ['column']
    elif axis == 1:
        na_summary.index.names = ['row']
    na_summary.reset_index(inplace=True)

    na_summary['na_perc'] = na_summary['na_count'] / df.shape[axis]

    return na_summary


def split_col_to_df_old(df, index_col, value_col, sep, add_col_prefix=False):
    """
    For columns that have multiple values per row, seperated by `sep`
    The functions splits them into a dataframe where columns represent all the possible values
    And the rows are the respondents, with the choice being represented as 1.
                      a   b   c   d
    1, a;b;c  ->   1,  1,  1,  1, NA
    2, d           2, NA, NA, NA, 1

    >>> import pandas as pd
    >>> df = pd.DataFrame({'index': [0, 1 , 2, 4], 'val': ['a;b;c', 'd', pd.np.NaN, '']})
    >>> split_col_to_df(df, 'index', 'val', sep=';')
    """
    new_df = []
    for idx, row in df[[index_col, value_col]].iterrows():
        options = ['']
        if not pd.isna(row[value_col]):
            options = row[value_col].split(sep)
        df = pd.DataFrame({value_col: options})
        df[index_col] = row[index_col]
        df['Count'] = 1
        new_df.append(df)

    new_df = pd.concat(new_df)
    new_df = new_df.pivot(index=index_col, columns=value_col, values='Count')

    if add_col_prefix:
        new_df.columns = [new_df]

    return new_df


def one_hot_encode(df, index_col, value_col, sep, add_col_prefix=False):
    """
    For columns that have multiple values per row, separated by `sep`
    The function splits them into a dataframe where columns represent all the possible values
    And the rows are the respondents, with the choice being represented as 1.
    idx|col       idx| a|  b|  c|  d
    1, a;b;c  ->   1,  1,  1,  1, NA
    2, d           2, NA, NA, NA, 1

    https://stackoverflow.com/a/56299184/6931113
    :param df:
    :param index_col:
    :param value_col:
    :param sep:
    :param add_col_prefix:
    :return:

    >>> import pandas as pd
    >>> df = pd.DataFrame({'index': [0, 1, 2, 4], 'val': ['a;b;c', 'd', pd.np.NaN, '']}, index=[10,20,30,40])
    >>> one_hot_encode(df, 'index', 'val', sep=';')
    """
    # TODO: this is memory inefficient
    new_df = df.copy()

    new_df['split'] = new_df[value_col].str.split(sep)
    new_df['split'] = new_df['split'].apply(lambda d: d if isinstance(d, list) else ['NA'])
    split_df = pd.get_dummies(new_df['split'].apply(lambda x: pd.Series(1, x)) == 1)

    if index_col:
        cols = split_df.columns.to_list()
        split_df[index_col] = new_df[index_col]
        split_df = split_df[[index_col] + cols]

    split_df.index = df.index

    return split_df
