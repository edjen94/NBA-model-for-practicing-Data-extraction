# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 02:07:23 2022

@author: jvsla
"""
import pandas as pd 
import numpy as np

dfgames=pd.read_csv('NBA_2012-2013_April.csv',usecols=['Home/Neutral','PTS.1','Visitor/Neutral','PTS'])
dfgames=dfgames[['Home/Neutral','PTS.1','Visitor/Neutral','PTS']]
dfgames.columns=['Team1','Team1score','Team2','Team2score']
dfstats=pd.read_csv('NBA_stats2012-13_7.csv',index_col=0)
dfstats=dfstats.drop(['TEAM_ID','CFID','CFPARAMS'],axis=1)


conditions=[
    dfgames['Team1score']>dfgames['Team2score'],dfgames['Team1score']<dfgames['Team2score']]

choices=[1,0]
dfgames['Homewin']=np.select(conditions,choices)

df=dfgames.merge(dfstats.add_prefix('Team1'),how='left',left_on=['Team1'],right_on=['Team1TEAM_NAME']).drop(['Team1TEAM_NAME'],axis=1).merge(dfstats.add_prefix('Team2'),how='left',left_on=['Team2'],right_on=['Team2TEAM_NAME']).drop(['Team2TEAM_NAME'],axis=1)

df=df.drop(['Team1','Team1score','Team2','Team2score'],axis=1)
#df.to_csv('2012-12_apr_merged.csv',index=False)



