from bs4 import BeautifulSoup
import mechanize
import pandas as pd
import datefinder

def get_data_from_web(url = '', starting_number = '', number_of_inquiries = 1):

	if url == '' or starting_number == '':
		return None

	inquiry_list = generate_inquiry_list(starting_number, number_of_inquiries)

	# print(inquiry_list)

	data_dict_list  = []
	for inquiry in inquiry_list:
		soup = get_soup(url, inquiry)
		print(inquiry)
		###### finding information #########
		paragraph = soup.find('div', class_ = 'rows text-center')
		# print(paragraph)
		case_status, date, form  = parse_paragraph (paragraph)
		dict_data = {}
		dict_data.update({'case_number': inquiry, 'case_status': case_status, 'date': date, 'form': form})
		data_dict_list.append(dict_data)

	df = pd.DataFrame(data_dict_list)  

	return df             

	##### output data ########

def get_soup (url = '', case_number = ''):
	## provide one case number and return one soup object ##

	br = mechanize.Browser()
	br.set_handle_robots(False)
	br.open(url)
	br.select_form(nr = 0)
	br['appReceiptNum'] = case_number
	response = br.submit()
	content = response.read()
	soup = BeautifulSoup(content, features = 'lxml')

	return soup 

def generate_inquiry_list(starting_number = '', number_of_inquiries = 5):

	if starting_number == '':
		return []

	inquiry_list = []

	for i in range(number_of_inquiries):
		inquiry_list.append(starting_number[:-5] + str(int(starting_number[-5:]) + i).zfill(5))
	return inquiry_list


def parse_paragraph (paragraph):
	if paragraph == None:
		return None, None, None
	contents = paragraph.p.text
	case_status = paragraph.h1.text
	dates = list(datefinder.find_dates(contents[:20]))
	if dates == []:
		date = ''
	else:
		date = dates[0].strftime("%Y/%m/%d")
	# print(contents[:20])

	contents_list = contents.split(' ')
	form = ''
	for i, item in enumerate(contents_list):
		if 'Form' in item:
			form = contents_list[i + 1]
			break
	# print(len(dates))
	return case_status, date, form


def write_soup_to_html(soup, export_file =''):
	pass





# url = "https://egov.uscis.gov/casestatus/landing.do"
# br = mechanize.Browser()
# br.set_handle_robots(False) # ignore robots
# br.open(url)
# br.select_form(nr = 0)
# br['appReceiptNum'] = 'LIN1990294588'
# res = br.submit()
# content = res.read()

# soup = BeautifulSoup(content, features = 'lxml')

 
# all_paragraphs = soup.find('div', class_ = 'rows text-center')

# print(type(all_paragraphs))
# print(all_paragraphs.h1.text)
# print(type(all_paragraphs.p.text))
# print(all_paragraphs.p.text)



# with open("mechanize_results.html", "wb") as f:
#     f.write(content)


# import requests
# from bs4 import BeautifulSoup

# # r = requests.get('https://egov.uscis.gov/casestatus/landing.do')


# payload = {'filed-box':'LIN1990294590'}
# #  = requests.post('http://httpbin.org/post', data = payload)

# r = requests.post('https://egov.uscis.gov/casestatus/landing.do', data = payload)
# # r = requests.get('https://egov.uscis.gov/casestatus/mycasestatus.do', data = payload)

# print(r)

# with open('data.html', 'wb') as f:
# 	f.write(r.content)

# soup = BeautifulSoup(r.text,'lxml')
# box = soup.find('div', class_ = 'filed-box')
# infor = soup.find('input', class_ = 'form-control textbox initial-focus') ## this is just like a dictionary
# status = soup.find('div', class_ = 'box3 uscis-seal')
# print(box.input)
# print(infor['type'])
# print(status)


# with requests.Session() as c:
# 	url = 'https://egov.uscis.gov/casestatus/landing.do'
# 	c.get(url)
# 	payload = {'filed-box':'LIN1990294590'}
# 	c.post(url, data=payload)
# 	# page = c.get('https://egov.uscis.gov/casestatus/mycasestatus.do')
# 	page = c.get(url)
# 	display = BeautifulSoup(page.text, 'lxml')
# 	print(display.prettify())

########## try mechanize ##############

	# url = "https://egov.uscis.gov/casestatus/landing.do"
	# br = mechanize.Browser()
	# br.set_handle_robots(False) # ignore robots
	# br.open(url)
	# br.select_form(nr = 0)
	# br['appReceiptNum'] = 'LIN1990294588'
	# res = br.submit()
	# content = res.read()

	# soup = BeautifulSoup(content, features = 'lxml')

	 
	# all_paragraphs = soup.find('div', class_ = 'rows text-center')

	# print(type(all_paragraphs))
	# print(all_paragraphs.h1.text)
	# print(type(all_paragraphs.p.text))
	# print(all_paragraphs.p.text)
