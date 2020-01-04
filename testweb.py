import datefinder

# s = 'On February 28, 2019, we received your Form I-765, Application for Employment Authorization, Receipt Number LIN1990294588, and sent you the receipt notice that describes how we will process your case.  Please follow the instructions in the notice.  If you do not receive your receipt notice by March 30, 2019, contact the USCIS Contact Center at www.uscis.gov/contactcenter.  If you move, go to www.uscis.gov/addresschange to give us your new mailing address.'

# matches = list(datefinder.find_dates(s))

# print(matches)

# # slist = s.split(' ')
# # print(slist)
# # for i, item in enumerate(slist):
# # 	if 'Form' in item:
# # 		form = slist[i + 1]
# # 		break
# # print(form)

# d = {}
# a = 1
# b = 2

# d.update({'a': a, 'b':b})

# print(d)


# s = 'LIN1990294588'

# sx = s[:-6] + str(int(s[-6:]) + 2)

# print(sx)
import pandas as pd 

s = 'On June 20, 2019,'
matches = list(datefinder.find_dates(s))
t = matches[0].strftime("%Y/%m/%d").replace('/','_')
print(t)
print(type(matches))

df = pd.DataFrame()
df.to_csv('{}.csv'.format(t))

import datetime

now = datetime.datetime.now()

print(str(now)[:10])


