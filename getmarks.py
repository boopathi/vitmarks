#!/usr/bin/

import requests
from HTMLParser import HTMLParser
class LinksParser(HTMLParser):
	def __init__(self):
		HTMLParser.__init__(self)
		self.recording = 0
		self.data = []

	def handle_starttag(self, tag, attributes):
		if tag != 'table':
			return
		if self.recording:
      			self.recording += 1
      			return
    		for name, value in attributes:
      			if name == 'width' and str(value) == '1100':
        			break
    		else:
     			 return
    		self.recording = 1

	def handle_endtag(self, tag):
    		if tag == 'table' and self.recording:
    			self.recording -= 1

  	def handle_data(self, data):
    		if self.recording:
      			self.data.append(data)

class vit(HTMLParser):
	def __init__(self):
		HTMLParser.__init__(self)
		self.recording = 0
		self.data = []
	def handle_start_tag(self, tag, attrs):
		if tag=='table':
			for name,value in attrs:
				if name=='width' and value=='1100':
					self.recording=1
	def handle_endtag(self,tag):
		if tag=='table':
			self.recording-=1
	def handle_data(self,data):
		if self.recording:
			self.data.append(data)

for i in range(1,2):
	payload = {'regno': '08BCE00'+str(i), 'genvrfcd':'abcdef', 'vrfcd': 'abcdef'}

	url="http://admission.vit.ac.in/myvit/fallsem1112/marks_report_submit.asp"
	r = requests.post(url, data=payload)
	p = LinksParser()
	p.feed(r.content)
	print ' '.join(p.data)
	p.close()
