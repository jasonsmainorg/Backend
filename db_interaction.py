#  DO NOT CHANGE ANY INSERT function once it has been created and ran

#Utilizing SQLAlchemy ORM for interfacing with Backend DataBase

import urllib.parse
from sqlalchemy import create_engine, Column, Integer, String, Float, BigInteger, Text
from sqlalchemy.orm import declarative_base, sessionmaker

# Connectivity to the Azure DB
import os
from dotenv import load_dotenv 
load_dotenv() 

server = os.getenv('AZURE_SQL_SERVER')
database = os.getenv('AZURE_SQL_DATABASE')
username = urllib.parse.quote_plus(os.getenv('AZURE_SQL_USER'))
password = urllib.parse.quote_plus(os.getenv('AZURE_SQL_PASSWORD'))
port = os.getenv('AZURE_SQL_PORT')

conn_str = f'mssql+pymssql://{username}:{password}@{server}/{database}'

engine = create_engine(conn_str)

# Base format for creating tables in ORM
Base = declarative_base()

class Game(Base):
    __tablename__ = 'steamspy'
    
    appid = Column(Integer, primary_key=True)
    name = Column(String(255))
    developer = Column(String(255))
    publisher = Column(String(255))
    score_rank = Column(Integer, nullable=True)
    positive = Column(BigInteger)
    negative = Column(BigInteger)
    userscore = Column(Float)
    owners = Column(String(255))
    average_forever = Column(Integer)
    average_2weeks = Column(Integer)
    median_forever = Column(Integer)
    median_2weeks = Column(Integer)
    price = Column(Float)
    initialprice = Column(Float)
    discount = Column(Integer)
    ccu = Column(Integer)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

import csv
with open('temp.csv','r') as inFile:
    for row in csv.reader(inFile):
        print(row)

session.close()