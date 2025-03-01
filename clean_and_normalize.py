from os.path import join
from os import listdir

import pandas as pd

from datetime import datetime
from tqdm import tqdm
from data_parsing import parse_allowance


def clean_and_normalize(csv_filename, input_dir, output_dir):
    
    df = pd.read_csv(join(input_dir,csv_filename))

    # Split dataframe into sugar babies and sugar daddies
    dfsb = df[df['I am a :'] == 'Sugar Baby Female']           
    dfsd = df[df['I am a :'] == 'Sugar Daddy']


    dfl = []
    for row in tqdm(dfsb.iterrows()):
        rd = row[1]
        # Parse string to datetime object
        output_dict = {
        #       'datetime': datetime.strptime(rd['Timestamp'], date_format),
                'datetime': rd['Timestamp'],
                'state': rd['Which state are you in?'],
                'city':rd['What city are you in'],
                'sb_race':rd['My race/ethnicity is:'],
                'sb_age':rd['My Age:'],
                'sb_marital_status':rd['My Marital Status:'],
                'sb_education':rd['Education Level:'],
                'sd_race':rd["My Partner's race/ethnicity is:"],
                'sd_age':rd["My Partner's Age:"],
                'sd_marital_status':rd["My Partner's Marital Status:"],
                'sd_education':rd["My Partner's Education Level:"],
                'time_together':rd['Length of Time Together'],
                'num_monthly_dates':rd['Number of Dates (Monthly)'],
                'Exclusive?':rd['Arrangement Questions [Are you Exclusive?]'],
                'More than one arrangement':rd['Arrangement Questions [Do you have more than one SR?]'],
                'Partner know real id?':rd['Arrangement Questions [Does your partner know your real Identity?]'],
                'Indoor Only?':rd['Arrangement Questions [Are your dates indoor only?]'],
                'Overnights or travel':rd['Arrangement Questions [Do you have overnight dates or travel together?]'],
                'More for Overnights or travel?':rd['Arrangement Questions [Do you give or receive more for overnights or travel?]'],
                'Gifts?':rd['Arrangement Questions [Do you give or receive gifts on top of allowance?]'],
                'Happy?':rd['How happy are you with your current arrangement?'],
                'Satisfied with give/receive?':rd['Are you satisfied with how much you receive or give financially?'],
                'Satisfied with time spent together?':rd['Are you satisfied with how much time you spend together?'],
                'Am I getting enough effort/support?':rd['I feel I am getting enough effort/financial support from my partner for the money I spend/effort I put into the relationship?'],

                'Allowance Type':rd['Allowance Type:'],
                'PPM/Weekly allowance':rd['PPM/Weekly Allowance Amount:'],
                'Allowance Amount':rd['Allowance Amount: (Actual amount received or given. Not total budget. For gifts and experience only arrangements select how much spent on a monthly basis.)'],
                'sample': 'sugar_baby'}

        dfl.append(output_dict)
    for row in tqdm(dfsd.iterrows()):
        rd = row[1]

        # Parse string to datetime object
        output_dict = {
    #       'datetime': datetime.strptime(rd['Timestamp'], date_format),
            'datetime': rd['Timestamp'],
            'state': rd['Which state are you in?'],

            'city':rd['What city are you in'],
            'sd_race':rd['My race/ethnicity is:'],
            'sd_age':rd['My Age:'],
            'sd_marital_status':rd['My Marital Status:'],
            'sd_education':rd['Education Level:'],
            'sb_race':rd["My Partner's race/ethnicity is:"],
            'sb_age':rd["My Partner's Age:"],
            'sb_marital_status':rd["My Partner's Marital Status:"],
            'sb_education':rd["My Partner's Education Level:"],
            'time_together':rd['Length of Time Together'],
            'num_monthly_dates':rd['Number of Dates (Monthly)'],
            'Exclusive?':rd['Arrangement Questions [Are you Exclusive?]'],
            'More than one arrangement':rd['Arrangement Questions [Do you have more than one SR?]'],
            'Partner know real id?':rd['Arrangement Questions [Does your partner know your real Identity?]'],
            'Indoor Only?':rd['Arrangement Questions [Are your dates indoor only?]'],
            'Overnights or travel':rd['Arrangement Questions [Do you have overnight dates or travel together?]'],
            'More for Overnights or travel?':rd['Arrangement Questions [Do you give or receive more for overnights or travel?]'],
            'Gifts?':rd['Arrangement Questions [Do you give or receive gifts on top of allowance?]'],
            'Happy?':rd['How happy are you with your current arrangement?'],
            'Satisfied with give/receive?':rd['Are you satisfied with how much you receive or give financially?'],
            'Satisfied with time spent together?':rd['Are you satisfied with how much time you spend together?'],
            'Am I getting enough effort/support?':rd['I feel I am getting enough effort/financial support from my partner for the money I spend/effort I put into the relationship?'],

            'Allowance Type':rd['Allowance Type:'],
            'PPM/Weekly allowance':rd['PPM/Weekly Allowance Amount:'],
            'Allowance Amount':rd['Allowance Amount: (Actual amount received or given. Not total budget. For gifts and experience only arrangements select how much spent on a monthly basis.)'],
            'sample': 'sugar_daddy'}

        dfl.append(output_dict)

    df = pd.DataFrame(dfl)

    lite_columns = [
                        'state',
                        'city',
                        'sb_race', 
                        'sb_age',
                        'sb_marital_status',
                        'sb_education',
                        'sd_race',
                        'sd_age',
                        'sd_marital_status',
           'sd_education', 'time_together', 'num_monthly_dates',  'Gifts?',
           'Happy?', 'Satisfied with give/receive?',
           'Am I getting enough effort/support?', 'Allowance Type',
           'PPM/Weekly allowance', 'Allowance Amount', 'sample'
           ]

    # reduce columns
    dfl = df[lite_columns] #df lite

    ll = [] # allowance list 2
    for row in dfl.iterrows():
        nmd, allowance_amount, per_meet_amount = parse_allowance(row)

        tdict = row[1].to_dict()
        tdict.update({'nmd':nmd,'allowance_amount':allowance_amount,'per_meet_amount':per_meet_amount})
        ll.append(tdict)

    dfl2 = pd.DataFrame(ll)

    dfl2.to_csv(join(output_dir,csv_filename),index=False)


if __name__ == "__main__":

    us_input_dir = './data/us/'
    us_output_dir = './data/us_lite/'

    us_files = listdir(us_input_dir)

    for f in us_files:
        clean_and_normalize(csv_filename=f, input_dir=us_input_dir, output_dir=us_output_dir)

    '''
    world_input_dir = './data/world/'
    world_output_dir = './data/world_lite/'

    world_files = listdir(world_input_dir)

    for f in world_files:
        clean_and_normalize(csv_filename=f, input_dir=world_input_dir, output_dir=world_output_dir)
    '''
