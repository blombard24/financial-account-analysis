import pandas as pd
import numpy as np

def retail_mapper(frame, targ_col, retail_col_name):
    '''
    assign retailer names to a new retailer column (retail_col_name) based on transaction name or description (targ_col)
    Keyword arguments:
    frame: DataFrame object
    targ_col: str - column containing transaction description or name this column will be pattern match to assign retailer names
    retail_col_name: str - new column which will be assigned the retailer name based on pattern matching in targ_col
    '''

    retailer_dict = {'ABC Pediatrics':['med.abc pediatrics ltd'],
                     'ABT Electronics':['abt electronics'],
                     'Acorn Tire and Service':['acorn tire'],
                     'Air Canada':['air canada','air can'],
                     'Air Transat':['air transat'],
                     'Akita Security':['akita securit',],
                     'Allegory':['allegory'],
                     'Amazon':['amazon','amzn mktp', 'amazon.com'],
                     'Audi Financial':['audi fincl'],
                     "Binny's Beverage Depoit":['binnys beverage depo',],
                     'Bobbie':['www.hibobbie.com'],
                     'Brown Bag Seafood':['brown bag seafood'],
                     'Caseys Foods': ['caseys foods'],
                     'City of Naperville':['city of naperville'],
                     'Comcast':['comcast'],
                     'Coopers Hawk':['coopershawk','coopers hawk wine'],
                     'Costco Wholesale':['costco whse'],
                     'Dollar Shave Club':['dollarshaveclub',],
                     'DoorDash':['dd doordash'],
                     'Dupage Medical Group':['dupage medical group'],
                     'Exxon Mobil':['exxonmobil'],
                     'Gia Mia':['gia mias'],
                     'Glo Nail Lounge':['glo nail lounge'],
                     'Hulu':['hulu.com/bill','amz.hulu llc'],
                     'Jewel Osco':['jewel osco'],
                     'Kesap Clean':['kesap clean'],
                     'Kids Kampus':['kids kampus'],
                     'Kidsnips':['kidsnips'],
                     "Kriser's Natural Pet":['krisers'],
                     'Linkedin':['linkedin pre'],
                     'Michael Graham Salon':['michael graham salon'],
                     'Nicor Gas':['nicor gas'],
                     'N/a':['amex epayment *ach','payment to chase card','payment thank you',
                            'purchase interest charge','online payment', 'american express ach pmt',
                            'foreign transaction fee','applecard gsbank payment','discover bank *prearrange',
                            'automatic payment - thank','chase credit crd autopay','autopay payment - thank you',
                            'atm withdrawal','discover e-payment web',],
                     'Peloton':['peloton. membership'],
                     'Play Room Cafe Two':['playroom cafe two'],
                     'Ritual':['ritual.com'],
                     'Riverbend Cafe: Edward Hospital':['riverbend caf .+naperville *il'],
                     'Roku':['roku for showtime digital'],
                     'Shred 415':['shred'],
                     'SIF Car Wash':['sif car care llc'],
                     'Sparrow Coffee':['sparrow coffee'],
                     'Starbucks Coffee':['starbucks'],
                     'Target':['target'],
                     'The Cleaning Authority':['the cleaning authority'],
                     'The Home Depot':['the home depot'],
                     'Travelers Insurance':['travelers per insur'],
                     'Uber':['uber *trip'],
                     'Whole Foods Market':['wholefds'],
                    }
        
    cond = [frame[targ_col].str.contains('|'.join(vals), case=False,regex=True) for vals in retailer_dict.values()]

    choice = list(retailer_dict)

    default_cond = pd.NA

    frame[retail_col_name] = np.select(condlist=cond, choicelist=choice, default=default_cond)

    return frame



def cat_mapper(frame, targ_col, cat_col):
    # retailer_aliases = {'amazon':['amazon','amzn mktp']}

    #category_retailers dictionary: keys will be the result for the category column while values will be the conditions used for key assignment

    # category_retailers = {'Online Shopping':['amazon','amzn mktp', 'target.com'],
    #                       'Wholesale Stores': ['costco', 'target'],
    #                       'Pet Stores':['krisers'],
    #                       'House Maintenance' : ['cleaning authority', 'j&b landscape'],
    #                       'Pet Care' : ['lucky dog daycare', 'eola point animal hosp'],
    #                       'Taxes' : ['dupage co tax'],
    #                       'Utilities':['nicor gas'],
    #                       'Kids: Daycare':['kids kampus'],
    #                       'Restaurant':['sparrow coffee'],
    #                       'Groceries: Alcohol':['binnys beverage'],
    #                       'Personal Care':['barber haus', 'michael graham salon'],
    #                       'Car Payment':['volvo car fin', 'audi fincl'],
    #                       'Income':['glanbia perform','wellmore holding'],
    #                       'Car Maintenance':['everwash'],
    #                       'Hardware Store':['ace hardware',],
    #                       'Bookstore':['andersons bksh'],
    #                       'Pharmacy':['walgreens'],
    #                       'Credit Card Payments':['applecard gsbank payment'],
    #                       'Loan Payment':['amex epayment ach a web',],
    #                       }
    
    category_retailers = {'ATM Cash Withdrawal':['atm withdrawal', 'atm withdraw',],
                          'Bookstore': ['andersons bksh'],
                          'Car Maintenance': ['everwash'],
                          'Car Payment': ['volvo car fin', 'audi fincl'],
                          'Credit Card Payments': ['applecard gsbank payment','payment to chase card','payment thank you',
                                                   'online payment - thank you','american express ach','automatic payment - thank',
                                                   'chase credit crd autopay','autopay payment - thank you',],
                          'Groceries: Alcohol': ['binnys beverage'],
                          'Hardware Store': ['ace hardware'],
                          'House Maintenance': ['cleaning authority', 'j&b landscape'],
                          'Income': ['glanbia perform', 'wellmore holding'],
                          'Insurance':['travelers per insur'],
                          'Kids: Daycare': ['kids kampus'],
                          'Kids: Entertainment':['playroom cafe two'],
                          'Loan Payment': ['amex epayment', 'ally lending'],
                          'Money Transfer':['DISCOVER BANK *PREARRANGE', 'kabbage *transfer',],
                          'Mortgage Payment':['First National Bank of Ottawa',],
                          'Online Shopping': ['amazon', 'amzn mktp', 'target.com'],
                          'Online Education': ['coursera.org',],
                          'Personal Care': ['barber haus', 'michael graham salon', 'glo nail lounge',], 
                          'Pet Care': ['lucky dog daycare', 'eola point animal hosp'], 
                          'Pet Stores': ['krisers'],
                          'Pharmacy': ['walgreens','oswalds pharmacy',],
                          'Restaurant': ['sparrow coffee'],
                          'Taxes': ['dupage co tax', 'il dept of reven', 'irs *treas',],
                          'Utilities': ['nicor gas'],
                          'Wholesale Stores': ['costco', 'target']}

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