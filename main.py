import speedtest
from datetime import datetime
import time
import pandas as pd
import os

here = os.getcwd()
if 'recs.csv' not in os.listdir(here):
    df = pd.DataFrame(columns = ['upload','download','provedor','cidade','hora','data'])
    df.to_csv('recs.csv')


df = pd.read_csv('recs.csv',index_col = 0)

now = datetime.now()
start_time = time.time()
s = speedtest.Speedtest()
date_string = now.strftime("%d/%m/%Y")
time_string = now.strftime("%H:%M")
dicionario = {'upload':round(s.upload()/1000000,2),'download':round(s.download()/1000000,2),'provedor':s.get_best_server().get('sponsor'),'cidade':s.get_best_server().get('name'),'hora':time_string,'data':date_string}
df = df.append(dicionario,ignore_index = True)
df.to_csv('recs.csv')
