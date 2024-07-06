import pandas as pd
import numpy as np
import os
import glob
from cleaners import *


def transaction_compiler():

    csv_file_list = []
    for i in os.listdir():
        if '.csv' in i.lower():
            csv_file_list.append(i)

    df = pd.DataFrame()

    col_lens = []

    for i in csv_file_list:

        # add column counts to a list for use in de-duplication later
        col_lens.append(pd.read_csv(i).shape[1])

        if 'amex' in i.lower():
            temp_df = pd.read_csv(i)
            
            temp_df = amex_credit_cleaner(temp_df)

            temp_df['file_name'] = i.split('.')[0]
            
            df = pd.concat([df, temp_df])

        elif ('chase' in i.lower()) & ('credit' in i.lower()):
            temp_df = pd.read_csv(i)
        
            # Transform to fit amex transactions
            temp_df = chase_credit_cleaner(temp_df)

            temp_df['file_name'] = i.split('.')[0]
        
            df = pd.concat([df, temp_df])
       
        elif ('chase' in i.lower()) & ('checking' in i.lower()):
            temp_df = pd.read_csv(i,index_col=False)
            temp_df = chase_checking_cleaner(temp_df)
            temp_df['file_name'] = i.split('.')[0]

            df = pd.concat([df, temp_df])
       
        elif ('fidelity' in i.lower()) & ('credit' in i.lower()):
            temp_df = pd.read_csv(i, index_col=False)
            temp_df = fidelity_credit_cleaner(temp_df)
            temp_df['file_name'] = i.split('.')[0]

            df = pd.concat([df, temp_df])

        elif ('clean' in i.lower()):
            temp_df = pd.read_csv(i, index_col=False)
            temp_df['Date'] = pd.to_datetime(temp_df['Date'])
            temp_df = temp_df.drop('Unnamed: 0', axis=1)
            df = pd.concat([df,temp_df])

    df = df.reset_index(drop=True)


    drop_col_list = df.columns[:max(col_lens)].to_list()


    df = df.drop_duplicates(subset=drop_col_list)


    return df