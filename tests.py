import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


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

def null_cat_plot(frame):
    
    mapped_frame = cat_mapper(frame, 'Description','Category')

    null_cats = mapped_frame.loc[mapped_frame['Category'].isnull()]


    #Remove all numbers from the description column to remove unique identifiers that could segment the descriptions unneccessarily
    null_cats.loc[:,'Description'] = null_cats['Description'].str.replace('[0-9]','', regex=True)
    #Remove extra whitepace between Description values and replace with a single whitespace
    null_cats.loc[:,'Description'] = null_cats['Description'].str.replace(r'\s+', ' ', regex=True)
    #Remove trailing and leading whitespace
    null_cats.loc[:,'Description'] = null_cats['Description'].str.strip()


    val_counts = null_cats.value_counts('Description')

    #Plot values 
    plt.figure(figsize=(6,4),dpi=200)
    sns.barplot(y = val_counts.index[:20], x= val_counts.values[:20],color='steelblue')

    #Formatting the plot
    plt.ylabel('Description', fontdict={'weight':500})
    plt.xlabel('Count', fontdict={'weight':500})
    plt.title('Count of Transactions without a Category',fontdict={'weight':900},loc='center')
    plt.yticks(fontsize=5)
    plt.xticks(fontsize=5)
    
    return plt.show()


def null_retailer_plot(frame):
    
    mapped_frame = retail_mapper(frame, 'Description','retailer')

    null_cats = mapped_frame.loc[mapped_frame['retailer'].isnull()]


    #Remove all numbers from the description column to remove unique identifiers that could segment the descriptions unneccessarily
    null_cats.loc[:,'Description'] = null_cats['Description'].str.replace('[0-9]','', regex=True)
    #Remove extra whitepace between Description values and replace with a single whitespace
    null_cats.loc[:,'Description'] = null_cats['Description'].str.replace(r'\s+', ' ', regex=True)
    #Remove trailing and leading whitespace
    null_cats.loc[:,'Description'] = null_cats['Description'].str.strip()


    val_counts = null_cats.value_counts('Description')

    #Plot values 
    plt.figure(figsize=(6,4),dpi=200)
    sns.barplot(y = val_counts.index[:20], x= val_counts.values[:20],color='steelblue')

    #Formatting the plot
    plt.ylabel('Description', fontdict={'weight':500})
    plt.xlabel('Count', fontdict={'weight':500})
    plt.title('Count of Transactions without a retailer',fontdict={'weight':900},loc='center')
    plt.yticks(fontsize=5)
    plt.xticks(fontsize=5)
    
    return plt.show()