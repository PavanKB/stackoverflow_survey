# StackOverflow Survey Analysis

This code base is meant to perform the EDA of the StackOverflow survey data.

Source: https://www.kaggle.com/stackoverflow/so-survey-2017

The repository is organised as below:

## so-survey-2017
1. **cty.csv**: The ISO codes for the countries in the data. Used for `choropleth` plot 
1. **survey_meta.csv**: additional meta data that was manually added after browsing the data.

## so
Contains the python scripts that used for extracting and manipulation data and for plotting. 

**Plotting**
* plot_data_dist_grid
* plot_col_dist
* plot_network_graph
* plot_chord_graph 

**Utils**
* get_col_unique_val
* get_na_summary
* split_col_to_df_old
* one_hot_encode

## data_exploration.ipynb
This is the jupyter python notebook that summarises the EDA of the stack_overflow 2017 dataset.  

