from bs4 import BeautifulSoup
import urllib
import re
import random

imagecount = 0
url = input('Please input a valid 4chan thread URL and press enter:')
thread_request = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'}) #spoof as firefox to avoid bot detection
thread_html = urllib.request.urlopen(thread_request).read()
thread_soup = BeautifulSoup(thread_html, 'html.parser')
for link in thread_soup.find_all('a'): 
	p = re.compile('\w+\\.(jpg|png|jpeg|gif|webm)$')
	if p.search(link['href']) is None:
		continue
	else:
		filename_regex = re.compile('\w+\\.(jpeg|jpg|gif|png|webm)$')
		filematch = filename_regex.search(link['href'])	
		if filematch is None:
			continue
		request = urllib.request.Request('http:' + link['href'], headers={'User-Agent': 'Mozilla/5.0'})
		print('Downloading ' + filematch.group() + '...')
		with open(filematch.group(), 'w+b') as result:
			imagefile = urllib.request.urlopen(request, timeout=random.randint(10, 25)).read()
			result.write(imagefile)
		imagecount = imagecount + 1
print('Done.')
print('Downloaded ' + str(imagecount) + ' images.')

