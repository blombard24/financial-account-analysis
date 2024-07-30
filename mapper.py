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
                     'Ace Hardware':['ace hardware','ace hardwanaperville'],
                     'Acorn Tire and Service':['acorn tire'],
                     'Air Canada':['air canada','air can'],
                     'Air Transat':['air transat'],
                     'Akita Security':['akita securit',],
                     'Allegory':['allegory'],
                     'Ally Lending':['ally lending'],
                     'Amazon':['amazon','amzn mktp', 'amazon.com'],
                     "Anderson's Bookstore":['andersons bksh'],
                     'Audi Financial':['audi fincl'],
                     "Bev's":['calis dba bevs'],
                     "Binny's Beverage Depoit":['binnys beverage depo',],
                     'Blackberry Market':['blackberry market',],
                     'Bobbie':['www.hibobbie.com'],
                     'Brown Bag Seafood':['brown bag seafood'],
                     'Caseys Foods': ['caseys foods','casey.s foods',],
                     'Chase Travel':['chase travel',],
                     'City of Naperville':['city of naperville'],
                     'Comcast':['comcast'],
                     'Coopers Hawk':['coopershawk','coopers hawk wine','coopers hawk','cooper.s hawk',],
                     'Costco Wholesale':['costco whse'],
                     'Coursera':['coursra.lzz.bfg.xpi',],
                     'Courtyard by Marriot':['courtyard santa monica','courtyard by marriot',],
                     'Dollar Shave Club':['dollarshaveclub',],
                     'DoorDash':['dd doordash'],
                     'Dupage County':['dupage co tax'],
                     'Dupage Medical Group':['dupage medical group','shs.dupagemedgrp',],
                     'Empyrean':['empyrean cobra *premiums',],
                     'Eola Point Animal Hospital':['eola point animal hosp'],
                     'Evereve':['^evereve'],
                     'Everwash':['everwash .+-*-.+ httpseverwash'],
                     'Exxon Mobil':['exxonmobil'],
                     'Floor and Decor':['floor and decor'],
                     'Gia Mia':['gia mias'],
                     'Glo Nail Lounge':['glo nail lounge'],
                     'hiya':['sp hiya health'],
                     'HomeGoods':['homegoods #'],
                     'Hulu':['hulu.com/bill','amz.hulu llc'],
                     'Illinois Tollway':['il tollway-autoreplenish'],
                     'Jewel Osco':['jewel osco'],
                     'J&B Landscape Solutions':['zelle payment to j&b landscape'],
                     'Kesap Clean':['kesap clean'],
                     'Kids Kampus':['kids kampus'],
                     'Kidsnips':['kidsnips'],
                     "Kohl's":['kohl.s'],
                     "Kriser's Natural Pet":['krisers'],
                     'Lacey Cafe':['3500 lacey - Cafe'],
                     'Le Chocolat du Bouchard':['le chocolat du'],
                     'Linkedin':['linkedin pre'],
                     'Loft':['loft .+main st', 'loft.com'],
                     'Longevity Spa':['longevity spa'],
                     'Lucky Dog Daycare':['lucky dog daycare'],
                     'Lululemon':['lululemon'],
                     "McDonald's":["mcdonald's"],
                     'Michael Graham Salon':['michael graham salon'],
                     'Nicor Gas':['nicor gas'],
                     'Not Applicable':['amex epayment *ach','payment to chase card','payment thank you',
                            'purchase interest charge','online payment', 'american express ach pmt',
                            'foreign transaction fee','applecard gsbank payment','discover bank *prearrange',
                            'automatic payment - thank','chase credit crd autopay','autopay payment - thank you',
                            'atm withdrawal','discover *e-payment .+web','kabbage *transfer *ppd','^check',
                            'thrivepass','remote online deposit','redemption credit','interest charge on purchases',
                            'mobile payment - thank you','. disney bundle credit','venmo *cashout *ppd',
                            'venmo *payment .+web','your cash reward/refund is','glanbia performa direct',
                            'wellmore holding direct', 'late fee',],
                     "Oswald's Pharmacy":['oswalds pharmacy'],
                     'Peloton':['peloton. membership'],
                     'Play Room Cafe Two':['playroom cafe two'],
                     'Rawsome Pets':['rawsomepets.net'],
                     'Ritual':['ritual.com'],
                     'Riverbend Cafe: Edward Hospital':['riverbend caf .+naperville *il'],
                     'Roku':['roku for showtime digital', 'the roku channel',],
                     'Sephora':['sephora'],
                     'Shell':['659 s washington st', '1707 s washington st','shell oil','shell service',],
                     'Shred 415':['shred'],
                     'SIF Car Wash':['sif car care llc'],
                     'Sparrow Coffee':['sparrow coffee'],
                     'Starbucks Coffee':['starbucks'],
                     'Target':['target'],
                     'The Cleaning Authority':['the cleaning authority'],
                     'The Growing Place':['the growing place',],
                     'The Home Depot':['the home depot'],
                     "Trader Joe's":['trader joe'],
                     'Travelers Insurance':['travelers *per *insur'],
                     'Uber':['uber *trip', 'uber',],
                     'United Airlines':['united [0-9]*'],
                     'Volvo Financial':['volvo car fin'],
                     "Walgreen's":['walgreens','walgreen',],
                     'Walmart':['walmart.com'],
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
                                                   'chase credit crd autopay','autopay payment - thank you',
                                                   'discover *e-payment .+web','mobile payment - thank you',],
                          'Groceries: Alcohol': ['binnys beverage'],
                          'Hardware Store': ['ace hardware'],
                          'Healthcare':['empyrean cobra *premiums'],
                          'House Maintenance': ['cleaning authority', 'j&b landscape'],
                          'Income': ['glanbia perform', 'wellmore holding'],
                          'Insurance':['travelers per insur'],
                          'Kids: Daycare': ['kids kampus'],
                          'Kids: Entertainment':['playroom cafe two'],
                          'Loan Payment': ['amex epayment', 'ally lending'],
                          'Money Transfer':['DISCOVER BANK *PREARRANGE', 'kabbage *transfer','venmo *cashout *ppd',
                                            ],
                          'Mortgage Payment':['First National Bank of Ottawa',],
                          'Online Shopping': ['amazon', 'amzn mktp', 'target.com'],
                          'Online Education': ['coursera.org',],
                          'Online Deposit':['remote online deposit'],
                          'Payment by Check':['^check'],
                          'Personal Care': ['barber haus', 'michael graham salon', 'glo nail lounge',], 
                          'Pet Care': ['lucky dog daycare', 'eola point animal hosp'], 
                          'Pet Stores': ['krisers'],
                          'Pharmacy': ['walgreens','oswalds pharmacy',],
                          'Reimbursements':['thrivepass *reimburse'],
                          'Restaurant': ['sparrow coffee'],
                          'Taxes': ['dupage co tax', 'il dept of reven', 'irs *treas',],
                          'Utilities': ['nicor gas'],
                          'Venmo Payment':['venmo *payment .+web',],
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