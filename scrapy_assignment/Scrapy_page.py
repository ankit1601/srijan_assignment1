from selenium import webdriver
from scrapy import Spider
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re
import pandas as pd
import os
import re

class pensylvania:#(Spider):
    name = 'pensylvania'
    start_urls = ['https://www.pafoodsafety.pa.gov/Web/Inspection/PublicInspectionSearch.aspx']
    Done=True
    def __init__(self):
        self.driver = webdriver.Chrome()

    def parse(self):#,response):
            	self.driver.get('https://www.pafoodsafety.pa.gov/Web/Inspection/PublicInspectionSearch.aspx')
             	try:
                    next = self.driver.find_element_by_xpath('//*[@id="MainContent_btnSearch"]')
                    next.click()
                    url = 'https://www.pafoodsafety.pa.gov/Web/Inspection/PublicInspectionSearch.aspx'
		    html = self.driver.page_source
		    soup_level1=BeautifulSoup(html,"lxml")
		    datalist = [] #empty list
		    x = 0 #counter
		    #print dir(soup_level1)
		    for table in soup_level1.find_all('table',id="MainContent_gvInspections"):
			#print dir(table)
			rows = table.findAll('tr')
			#matches = ([nonformattednameaddress]+="[]")\w+
			regex = re.compile(r'''((nonformattednameaddress+="(.*?)")+)''')
			matches = regex.findall(str(rows))
			print type(matches)
			for x in matches:
				print "############################"
				print x[0].split('=')[1]
			print len(matches)
			matchesVal = [x[0].split('=')[1] for x in matches]
			df1 = pd.DataFrame(matchesVal,columns=['Name / Address'])
			df1.drop_duplicates(inplace=True)
			#inputTags =  rows.find(attrs={"name":"nonformattednameaddress"})
			#df = pd.read_html(str(table),header=0) # this was giving all the data but format was not good 
			#print len(df)
			#print df
			#for dt in df:
			    #print "***********************************************************"
			    #dt.columns
			    #dt.dropna(inplace=True,axis=1) 
			    #print dt
			    #print dt.columns
			    #with open('mydata.csv','a') as f: 
			df1[['Name / Address']].to_csv('mydata.csv',sep=',',header=True,index=False,mode='a')
                    #yield Request(url,callback=self.parse2)
                except Exception,e:
		    print e
	        self.Done=False	
	        self.driver.close()
if __name__=="__main__":
    Scrap = pensylvania();
    Scrap.parse()

