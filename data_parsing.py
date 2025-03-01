from numpy import isnan

'''
num_monthly_dates
['3-4' '10+' '1-2' '5-6' '7-8' '9-10']
map_nmd={'3-4':3.5, '10+':10, '1-2':1.5,'5-6':5.5, '7-8':7.5, '9-10':9.5}
Allowance Type
['Pay Per Meet (PPM)' 'Gifts and Experiences' 'Weekly Allowance'
 'Monthly Allowance']
PPM/Weekly allowance
['$1k - $1,999' '$2k - $2,999' '$400-$499' nan '$300-$399' '$600-$699'

 '$500-$599' '$1k or more' '< $300' '$800-$899' '$700-$799']

Allowance Amount
[nan '$1k- $1,999' '$2k-$2,999' '$3k-$3,999' '$10k or more' '$5k-$5,999'
 '$4k-$4,999' '$6k-$6,999']
'''

map_nmd={'3-4':3.5,
         '10+':10,
         '1-2':1.5,
         '5-6':5.5,
         '7-8':7.5,
         '9-10':9.5}

ppm_map={'$1k- $1,999':1500, 
         '$1k - $1,999':1500, 
         '$2k-$2,999':2500, 
         '$2k - $2,999':2500, 
         '$400-$499':450,
         '$300-$399':350,
         '$600-$699':650,
         '$500-$599':550,
         '$1k or more':1000,
         '< $300':150 ,
         '$800-$899':850,
         '$700-$799':750,
        '$900-$999':950,
         '$3k or more':3500
        }

all_map = {'$1k- $1,999':1500,
           '$1k - $1,999':1500, 
          '$2k-$2,999': 2500,
          '$2k - $2,999':2500, 
          '$3k-$3,999':3500,
          '$10k or more':10000,
          '$5k-$5,999':5500,
          '$4k-$4,999':4500,
           '$6k-$6,999':6500,
           '$8-$8.999': 8500,
           '$9k-$9,999':9500,
            '$7k-$7,999':7500
          }

def parse_allowance(input_row):
    
    row = input_row[1]

    at = row['Allowance Type']

    nmd = map_nmd[row['num_monthly_dates']]

    match at:
        case 'Pay Per Meet (PPM)':
            
            per_meet_amount = ppm_map[row['PPM/Weekly allowance']]
            allowance_amount=nmd*per_meet_amount
            #print ("nmd {} pma {} allowance {}".format(nmd,per_meet_amount,allowance_amount))

        case 'Gifts and Experiences':

            if isnan(row['PPM/Weekly allowance']):
                allowance_amount=all_map[row['Allowance Amount']]
                per_meet_amount =allowance_amount/nmd 
            else:
                per_meet_amount = ppm_map[row['PPM/Weekly allowance']]
                allowance_amount=nmd*per_meet_amount
            #print ("nmd {} pma {} allowance {}".format(nmd,per_meet_amount,allowance_amount))

        case 'Weekly Allowance':
            allowance_amount = 4*ppm_map[row['PPM/Weekly allowance']]
            per_meet_amount = allowance_amount / nmd
            #print ("nmd {} pma {} allowance {}".format(nmd,per_meet_amount,allowance_amount))
        case 'Monthly Allowance':
            allowance_amount = all_map[row['Allowance Amount']]
            per_meet_amount = allowance_amount / nmd
    return nmd, allowance_amount, per_meet_amount
