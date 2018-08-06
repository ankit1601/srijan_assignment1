from selenium import webdriver
from scrapy import Spider
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re
import pandas as pd
import os

class pensylvania:#(Spider):
    name = 'pensylvania'
    start_urls = ['https://www.pafoodsafety.pa.gov/Web/Inspection/PublicInspectionSearch.aspx']
    Done=True
    def __init__(self):
        self.driver = webdriver.Chrome()

    def parse(self):#,response):
            	self.driver.get('https://www.pafoodsafety.pa.gov/Web/Inspection/PublicInspectionSearch.aspx')
            #while self.Done:
             	try:
                    next = self.driver.find_element_by_xpath('//*[@id="MainContent_btnSearch"]')
                    next.click()
                    url = 'https://www.pafoodsafety.pa.gov/Web/Inspection/PublicInspectionSearch.aspx'
		    #print "#########################################################################"
		    html = self.driver.page_source
		    #print html
		    soup_level1=BeautifulSoup(html,"lxml")
		    #print soup_level1
		    datalist = [] #empty list
		    x = 0 #counter
		    #print dir(soup_level1)
		    for table in soup_level1.find_all('table',id="MainContent_gvInspections"):
			#print dir(table)
			rows = table.findAll('tr')
			#inputTags =  rows.find(attrs={"name":"nonformattednameaddress"})
			#print inputTags
			#print output = [x['nonformattednameaddress'] for x in inputTags]
			df = pd.read_html(str(table),header=0)
			print len(df)
			print df
			for dt in df:
			    print "***********************************************************"
			    #dt.columns
			    dt.dropna(inplace=True,axis=1) 
			    #print dt
			    print dt.columns
			    with open('mydata.csv','a') as f: 
			        dt[['Name / Address']].to_csv('mydata.csv',sep=',',header=True,index=False,mode='a')
				break
		    #print dir(self.driver.page_source)
		    #print "this is the type######################"
		    #print type(html)
		    #print html
                    #yield Request(url,callback=self.parse2)
                except Exception,e:
		    print e
                    #break
	        self.Done=False	
	        self.driver.close()
if __name__=="__main__":
    Scrap = pensylvania();
    Scrap.parse()

    #def parse2(self,response):
	#print "You are here******************************"
        #print response.body
