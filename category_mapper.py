import pandas as pd
import numpy as np

def cat_mapper(frame, targ_col, cat_col):
    # retailer_aliases = {'amazon':['amazon','amzn mktp']}

    #category_retailers dictionary: keys will be the result for the category column while values will be the conditions used for key assignment

    category_retailers = {'Online Shopping':['amazon','amzn mktp', 'target.com'],
                          'Wholesale Stores': ['costco', 'target'],
                          'Pet Stores':['krisers'],
                          'House Maintenance' : ['cleaning authority', 'j&b landscape'],
                          'Pet Care' : ['lucky dog daycare', 'eola point animal hosp'],
                          'Taxes' : ['dupage co tax'],
                          'Utilities':['nicor gas'],
                          'Kids: Daycare':['kids kampus'],
                          'Restaurant':['sparrow coffee'],
                          'Groceries: Alcohol':['binnys beverage'],
                          'Personal Care':['barber haus', 'michael graham salon'],
                          'Car Payment':['volvo car fin', 'audi fincl'],
                          'Income':['glanbia perform','wellmore holding'],
                          'Car Maintenance':['everwash'],
                          'Hardware Store':['ace hardware',],
                          'Bookstore':['andersons bksh'],
                          'Pharmacy':['walgreens'],
                          'Credit Card Payments':['applecard gsbank payment']
                          }

    # retailer_cats = {'amazon':' Shopping'}

    # cond = [
    #     frame[targ_col].str.contains('|'.join(category_retailers['Online Shopping']),regex=True,case=False),
    #     frame[targ_col].str.contains('|'.join(category_retailers['Wholesale Stores']),regex=True,case=False),
    #     frame[targ_col].str.contains('|'.join(category_retailers['Pet Stores']),regex=True,case=False),
    #     frame[targ_col].str.contains('|'.join(category_retailers['House Maintenance']),regex=True,case=False),
    #     frame[targ_col].str.contains('|'.join(category_retailers['Pet Care']),regex=True,case=False),
    #     frame[targ_col].str.contains('|'.join(category_retailers['Taxes']),regex=True,case=False),
    #     frame[targ_col].str.contains('|'.join(category_retailers['Utilities']),regex=True,case=False),
    #     frame[targ_col].str.contains('|'.join(category_retailers['Kids: Daycare']),regex=True,case=False),
    # ]

    # choice = [
    #     'Online Shopping',
    #     'Wholesale Stores',
    #     'Pet Stores',
    #     'House Maintenance',
    #     'Pet Care',
    #     'Taxes',S
    #     'Utilities',
    #     'Kids: Daycare',
    # ]

    cond = [frame[targ_col].str.contains('|'.join(i), regex=True, case=False) for i in category_retailers.values()]

    choice = list(category_retailers)

    default_cond = frame[cat_col]

    frame[cat_col] = np.select(cond, choice, default_cond)

    return frame