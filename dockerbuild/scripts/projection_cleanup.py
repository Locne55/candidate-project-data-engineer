# -*- coding: utf-8 -*-
import sqlalchemy as sql
import sqlalchemy.dialects.postgresql as psql
import pandas as pd
import xmltodict

#create engine for reading postgres tables into dataframes
engine = sql.create_engine('postgresql+psycopg2://postgres:123@db:5432/postgres')

#read projections table into df1
df1 = pd.read_sql(sql='select * from projections', con=engine)

#parse xml to create a dict
data=xmltodict.parse(df1['xml'][0])

#flatten xml schema into columns
data2=pd.json_normalize(data)

#flatten xml data column into dataframe
finaldf = pd.DataFrame.from_dict(data2.iloc[0,-1:][0])
finaldf.columns = finaldf.columns.str.replace('@','')


finaldf.to_sql('projections_cleaned', engine, index_label = 'projectionid_cleaned', dtype={
    'projectionid_cleaned':psql.INTEGER,
    'Description':psql.VARCHAR,
    'Projected': psql.MONEY,
    'Deposit' : psql.MONEY,
    'MonthYear': psql.TIMESTAMP,
    'Payment': psql.MONEY},
               if_exists='replace')