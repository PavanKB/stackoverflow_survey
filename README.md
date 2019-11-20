# StackOverflow Survey Analysis

This code base is meant to perform the EDA of the StackOverflow survey data.

Source: https://www.kaggle.com/stackoverflow/so-survey-2017

The repository is organised as below:

## so-survey-2017
1. **cty.csv**: The ISO codes for the countries in the data. Used for `choropleth` plot 
1. **survey_meta.csv**: additional meta data that was manually added after browsing the data.

## so
Contains the python scripts that used for extracting and manipulation data and for plotting. 

### Packages used
* `pandas`
* `itertools`
* `collections`
* `matplotlib`
* `seaborn`
* `plotly`
* `networkx`
* `holoviews`
* `colorcet`


Description of the files:


### `utils.py`
* **`get_col_unique_val`**

Extracts the unique values per column in df and returns them as dict.
This also takes care of the cases where multiple values are stored as ; separated strings.
Used to get the meta data.

* **`get_na_summary`**

Calculates the number of NA values and the % by rows or columns.
Can be used to decide columns/rows to drop. 

* **`split_col_to_df_old`**

Older function to split the multiple values column into one hot encoded 
data frame. see `one_hot_encode`

* **`one_hot_encode`**

Used for columns that store multiple values as `;` separated string.
It converts them into a one hot encoded string.

### `plotting.py`
* **`plot_col_dist`**

Creates a count plot of the distinct values in the column.
* **`plot_data_dist_grid`**

Same as `plot_col_dist` but squeezes multiple plots into one.
Good for combining similar plot into a summary.

Plot multiple columns count plot as a grid.
* **`plot_network_graph`**

Creates a network graph of the variables in multiple options response.
These are usually stored as '; ' separated value in each row.
The thickness of the edge corresponds to the number of connections.

* **`plot_chord_graph`**

Plots a chord plot for the different categories, a different of visualising the network.
    

* **`plot_choropleth`**

Plots the world map,with the colour representing the count of the variables.


* **`plot_facet`** 

Plots a facet graph (histogram) to help with analysis based on a variable.

## data_exploration.ipynb
This is the jupyter python notebook that summarises the EDA of the stack_overflow 2017 dataset.  

