#!/usr/bin/

import requests, re
from BeautifulSoup import BeautifulSoup
import sys
for i in range(1, int(sys.argv[1]) + 1 ):
	num = ""
	if i<10:
		num = "00" + str(i)
	elif i<100:
		num = "0" + str(i)
	else:
		num = str(i)
	payload = {'regno': '08BCE'+num, 'genvrfcd':'abcdef', 'vrfcd': 'abcdef'}

	url="http://admission.vit.ac.in/myvit/fallsem1112/marks_report_submit.asp"
	r = requests.post(url, data=payload)
	da = BeautifulSoup(r.content)
	found = da.findAll('table')
	print "<h1>" + str(i) + "</h1>"
	print "<table>"
	for it in found:
		if 'width="1100"' in str(it) and not 'width="100%"' in str(it):
			trs=it.findAll('tr')
			for j in trs[2:]:
				tds=j.findAll('td')
				print "<tr><td> "
				print str(tds[2]).lstrip("<td>").rstrip("</td>") + " " + str(tds[-1]).strip("<td>").rstrip("</td>") + " "
				m = re.search('<!--(.)*-->',str(j))
				print m.group(0).lstrip("<!--<td>").rstrip("</td>-->")
				print " </td></tr>"
	print "</table>"
