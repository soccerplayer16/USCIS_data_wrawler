from web_search_tools import get_data_from_web
import pandas as pd
import time
import datetime

now = datetime.datetime.now()
today_date = str(now)[:10].replace('-','_')

start_time = time.time()

url = 'https://egov.uscis.gov/casestatus/landing.do'

starting_number = 'LIN1990280000'

number_of_queries = 20

df = get_data_from_web(url, starting_number, number_of_queries)

# print(df)

df.to_csv('data_{}_{}.csv'.format(today_date,starting_number))

## roughly 1.25s per item ##

print("--- %s seconds ---" % (time.time() - start_time))