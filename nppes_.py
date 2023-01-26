import requests
import pandas as pd
import csv

#the npis used to pull for
npi_list = []

#this was to just look at whats pulled
for x in npi_list:
    response = requests.get(f'https://npiregistry.cms.hhs.gov/api/?version=2.1&number={x}&pretty=on')
    print('NPI:' ,response.json()['results'][0]['number'],
          '| first_name:', response.json()['results'][0]['basic']['first_name'],
          '| last_name:', response.json()['results'][0]['basic']['last_name'],
          '| taxonomy_code:', response.json()['results'][0]['taxonomies'][0]['code'],
          '| desc:', response.json()['results'][0]['taxonomies'][0]['desc'],
          '| license_num:', response.json()['results'][0]['taxonomies'][0]['license']
         )

#creating the DataFrame
data = {'npi': [], 'first_name': [], 'last_name': [], 'taxonomy_code': [], 'description': [], 'license_number': []}
df = pd.DataFrame(data)
df

#this will add the each npi based pull into the above created new dataframe
for x in npi_list:
    response = requests.get(f'https://npiregistry.cms.hhs.gov/api/?version=2.1&number={x}&pretty=on')
    df = df.append({'npi': response.json()['results'][0]['number'],
                    'first_name': response.json()['results'][0]['basic']['first_name'],
                    'last_name': response.json()['results'][0]['basic']['last_name'],
                    'taxonomy_code': response.json()['results'][0]['taxonomies'][0]['code'],
                    'description': response.json()['results'][0]['taxonomies'][0]['desc'],
                    'license_number': response.json()['results'][0]['taxonomies'][0]['license']
                   }, ignore_index=True)

#viewing it looks good
df

#saves it to the script location
df.to_csv('NPPES_API_PULL.csv',index=False)