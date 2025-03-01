import pandas as pd
from tqdm import tqdm

# Data gathered feb 28 2024

data_folder = './data/us/'

links = {
    'northeast':'https://docs.google.com/spreadsheets/d/e/2PACX-1vTxSwwy7_bSXvItCtRC3tw0ZcN5QLCpDNnmnWEKF03CR_SYi3t8CR3bMVO1VCHwT4nRaePk6J2WY07O/pubhtml',
    'rocky_mountains':'https://docs.google.com/spreadsheets/d/e/2PACX-1vRL_qGCGl3EJuhQMMckWGWnzn4fW7qYONpo9UuIe4WNDPpZI8TaYC4l5vQkz0UMZyu6p7GCRCB_RRkv/pubhtml',
    'southeast':'https://docs.google.com/spreadsheets/d/e/2PACX-1vSjMBhlEULce2oAIjd4LQA1zVI_c0pBZfP5vQ_NKsi2jpK-6X0a7ZM8YZ6c3jeBIIqzy4Hz1PUc0-NF/pubhtml',
    'southwest':'https://docs.google.com/spreadsheets/d/e/2PACX-1vRL_qGCGl3EJuhQMMckWGWnzn4fW7qYONpo9UuIe4WNDPpZI8TaYC4l5vQkz0UMZyu6p7GCRCB_RRkv/pubhtml',
    'west_coast':'https://docs.google.com/spreadsheets/d/e/2PACX-1vS6ysoJ8w-Uuwf1ZZdKnwvyWK--HhQuf-ZzEFZRiVEg7rWcuWsYf78iyadNToPxkgiNiMw2zTdM-9eG/pubhtml',
    'mid_atlantic':'https://docs.google.com/spreadsheets/d/e/2PACX-1vRxHBXH81MpJiqR4j1mc1wjIRjW2lUXY9x5tBLzmebGI7Z8lSZt3qFCnSaa5gnxB_ZX6oTk96nBLZVf/pubhtml',
    'mid_west':'https://docs.google.com/spreadsheets/d/e/2PACX-1vQMbBlILKbUNRqOFXrlvxaaviXYVm-vmgIJXB0i5hQeEX9J7gExFS4rq_LWiotoNmqqF_uQ5m8TMNk5/pubhtml',
    'noncontiguous':'https://docs.google.com/spreadsheets/d/e/2PACX-1vT4_DcCDTYR26AehZp3oo3DYYRHlYGOKR9-y3vvXBkl3rgsdEe2mJ4ejomXc7ntElevpyWf2Kj2WzGw/pubhtml'
}

def get_csv(name,url):

    tables = pd.read_html(url)

    df = tables[0]

    df.columns = df.iloc[0]
    df = df[1:].reset_index(drop=True)

    df.to_csv(data_folder+'{}.csv'.format(name))

for k,v in tqdm(links.items()):

    get_csv(name=k,url=v)
