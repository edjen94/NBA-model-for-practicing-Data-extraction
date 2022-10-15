# -*- coding: utf-8 -*-
"""
Created on Sat Aug  6 06:39:19 2022

@author: jvsla
"""
#to open url and creating requests 
import urllib.request

from pprint import pprint 
#parsing tables from website
from html_table_parser.parser import HTMLTableParser
import pandas as pd 

def url_get_contents(url):
 
    req = urllib.request.Request(url=url)
    f = urllib.request.urlopen(req)

    return f.read()
# defining the html contents of a URL.
month='april'
xhtml = url_get_contents('https://www.basketball-reference.com/leagues/NBA_2013_games-'+str(month)+'.html').decode('utf-8')
 
# Defining the HTMLTableParser object
p = HTMLTableParser()
 
# feeding the html contents in the
# HTMLTableParser object
p.feed(xhtml)
 
df=pd.DataFrame(p.tables[0]) 
df.columns=df.iloc[0]
df=df.drop(index=0)

df=df.drop(df[['Date','Arena','','Notes']],axis=1)
df.to_csv('NBA_2012-2013_April.csv')


