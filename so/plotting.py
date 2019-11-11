import matplotlib.pyplot as plt
import seaborn as sns


def plot_data_dist_grid(data, col_idx, n_col=4, n_row=4, order=None):
    # Create the subplot to host the plots.
    fig, axes = plt.subplots(nrows=n_row, ncols=n_col, figsize=[25, 20])

    n_plot = n_row * n_col
    plot_idx = [x for x in range(0, n_plot)]

    if len(col_idx) > n_plot:
        print('More columns than available plots.')

    mapping = dict(zip(col_idx[0:n_plot], plot_idx))

    for c_idx, p_idx in mapping.items():
        # doing this to avoid the error
        plot_data = data[[c_idx]].copy(deep=True)
        plot_data.fillna('NA', inplace=True)
        if order:
            g = sns.countplot(x=c_idx, data=plot_data, ax=axes.flatten()[mapping[c_idx]], order=order)
        else:
            g = sns.countplot(x=c_idx, data=plot_data, ax=axes.flatten()[mapping[c_idx]])
        _ = g.set_xticklabels(rotation=30, labels=g.get_xticklabels())


def plot_col_dist(df, col_idx, order=None, sort=True, rotation=90, fig_size=(10, 5)):
    # Create the subplot to host the plots.
    fig, ax = plt.subplots(figsize=fig_size)

    if order:
        g = sns.countplot(data=df, x=col_idx, order=order, ax=ax)
    else:
        if sort:
            order = df[col_idx].value_counts().index
            g = sns.countplot(data=df, x=col_idx, order=order, ax=ax)
        else:
            g = sns.countplot(data=df, x=col_idx, ax=ax)

    _ = g.set_xticklabels(rotation=rotation, labels=g.get_xticklabels())
