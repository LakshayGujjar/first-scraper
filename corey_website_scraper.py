#scaping corey's website
import requests
from bs4 import BeautifulSoup

#grabing url
source=requests.get('https://coreyms.com/')

#scraping data
doc=source.text
soup=BeautifulSoup(doc,'lxml')

#print(soup.prettify())

for article in soup.find_all('article'):
	headline=article.h2.a.text
	print(headline)

	summary=article.find('div',class_='entry-content').p.text
	print(summary)

	print()
	#note an error could occur if some thing is empty say no youtube link
	#that is
	#  vid_src=article.find('iframe',class_='youtube-player')['src']
	#TypeError: 'NoneType' object is not subscriptable
	try:
		vid_src=article.find('iframe',class_='youtube-player')['src']
	#becaz it output a dict of attribute and we are grabing srcc out of dict

	#process to create a link from youtube embedd video using its id
		vid_id=vid_src.split('/')[4]
		vid_id=vid_id.split('?')[0]

		vid_link=f'https://youtube.com/watch?v={vid_id}'

	except Exception as e:
		vid_link=None

	print(vid_link)
	



