import pandas as pd
import numpy as np


def fidelity_credit_cleaner(frame):
    frame = frame.rename(columns={'Name':'Description'})
    frame['Date'] = pd.to_datetime(frame['Date'])
    return frame

def chase_checking_cleaner(frame):
    frame = frame.rename(columns={'Posting Date': 'Date'})
    frame['Date'] = pd.to_datetime(frame['Date'])
    return frame

def chase_credit_cleaner(frame):
    frame = frame.drop('Post Date',axis=1)
    frame = frame.drop('Memo', axis=1)
    
    frame = frame.rename(columns={'Transaction Date':'Date'})
    frame['Date'] = pd.to_datetime(frame['Date'])
    # frame['Amount'] = frame['Amount'] * -1
    return frame

def amex_credit_cleaner(frame):
    frame['Date'] = pd.to_datetime(frame['Date'])
    frame['Amount'] = frame['Amount'] * -1
    return frame