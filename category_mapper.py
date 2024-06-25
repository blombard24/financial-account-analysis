import pandas as pd
import numpy as np

def cat_mapper(frame, targ_col, cat_col):
    # retailer_aliases = {'amazon':['amazon','amzn mktp']}

    category_retailers = {'Online Shopping':['amazon','amzn mktp', 'target.com'],
                          'Wholesale Stores': ['costco', 'target'],
                          'Pet Stores':['krisers'],
                          'House Maintenance' : ['cleaning authority'],
                          'Pet Care' : ['lucky dog daycare'],

                          }

    # retailer_cats = {'amazon':' Shopping'}

    cond = [
        frame[targ_col].str.contains('|'.join(category_retailers['Online Shopping']),regex=True,case=False),
        frame[targ_col].str.contains('|'.join(category_retailers['Wholesale Stores']),regex=True,case=False),
        frame[targ_col].str.contains('|'.join(category_retailers['Pet Stores']),regex=True,case=False),
        frame[targ_col].str.contains('|'.join(category_retailers['House Maintenance']),regex=True,case=False),
        frame[targ_col].str.contains('|'.join(category_retailers['Pet Care']),regex=True,case=False),
    ]

    choice = [
        'Online Shopping',
        'Wholesale Stores',
        'Pet Stores',
        'House Maintenance',
        'Pet Care',
    ]

    default_cond = frame[cat_col]

    frame[cat_col] = np.select(cond, choice, default_cond)

    return frame