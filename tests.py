import pandas as pd
import numpy as np

from mapper import *


#Test effect of mappers by calculating null counts before and after mappers are applied

def map_test(frame):

    temp_df = frame.copy()

    ## add any new columns to og_null_count that will be added by mappers so they get included in the final null count
    og_null_count = temp_df.copy()

    new_cols = ['retailer']

    og_null_count[new_cols] = pd.NA

    #Create a dateframe with the original null counts
    og_null_count = og_null_count.isnull().sum()
    og_null_count = og_null_count.to_frame('original_null_count')
    
    #All category mappers below
    temp_df = cat_mapper(temp_df, 'Description','Category')

    temp_df = retail_mapper(temp_df, 'Description','retailer')

    #Calculate new null counts and join to original nulls counts to compare

    new_null_count = temp_df.isnull().sum().to_frame('cleaned_null_count')
    null_count_df = og_null_count.merge(new_null_count, left_index=True, right_index=True)
    null_count_df['percent_null_count_difference'] =round((null_count_df['original_null_count']-null_count_df['cleaned_null_count'])/null_count_df['original_null_count'],2)
    null_count_df['percent_null_count_difference'] = null_count_df['percent_null_count_difference'].fillna(0.00)

    return null_count_df