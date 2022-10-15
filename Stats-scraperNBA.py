# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 04:17:11 2022

@author: jvsla
"""

import requests
import pandas as pd 

season_id='2012-13'

month=[1,2,3,4,5,6,7]


for i in month:
    team_url='https://stats.nba.com/stats/leaguedashteamstats?Conference=&DateFrom=&DateTo=&Division=&GameScope=&GameSegment=&LastNGames=0&LeagueID=00&Location=&MeasureType=Advanced&Month='+str(i)+'&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=PerGame&Period=0&PlayerExperience=&PlayerPosition=&PlusMinus=N&Rank=N&Season='+str(season_id)+'&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&StarterBench=&TeamID=0&TwoWay=0&VsConference=&VsDivision='
    
    headers  = {
        'Connection': 'keep-alive',
        'Accept': 'application/json, text/plain, */*',
        'x-nba-stats-token': 'true',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
        'x-nba-stats-origin': 'stats',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Referer': 'https://stats.nba.com/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
    }
    
    response= requests.get(url=team_url,headers=headers).json()
    team_info= response['resultSets'][0]['rowSet']
    column_name=response['resultSets'][0]['headers']
    df=pd.DataFrame(team_info,columns=column_name)
    df.to_csv('NBA_stats'+str(season_id)+'_'+str(i)+'.csv')
