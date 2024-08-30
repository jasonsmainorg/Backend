#  DO NOT CHANGE ANY INSERT function once it has been created and ran

import urllib.parse
from sqlalchemy import create_engine, Column, Integer, String, Float, BigInteger, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import urllib, os

from dotenv import load_dotenv 
load_dotenv() 

driver='{ODBC Driver 18 for SQL Server}'
server = os.getenv('AZURE_SQL_SERVER')
database = os.getenv('AZURE_SQL_DATABASE')
username = os.getenv('AZURE_SQL_USER')
password = os.getenv('AZURE_SQL_PASSWORD')
port = os.getenv('AZURE_SQL_PORT')


Base = declarative_base()

class Game(Base):
    __tablename__ = 'games'
    
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

# Replace 'your_connection_string' with your Azure SQL Database connection string

conn_str='mmsql+pyodbc::///?odbc_connect='+urllib.parse.quote_plus(
    'Driver=%s;' % driver +
    'Server=tcp:%s,1433;' % server +
    'Database=%s;' % database +
    'Uid=%s;' % username +
    'Pwd={%s};' % password +
    'Encrypt=yes;' +
    'TrustServerCertificate=no;' +
    'Connection Timeout=30;')
engine = create_engine(conn_str)
# Base.metadata.create_all(engine)

# Session = sessionmaker(bind=engine)
# session = Session()
