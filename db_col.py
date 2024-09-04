import urllib.parse
from sqlalchemy import create_engine, Column, Integer, String, Float, Text
from sqlalchemy.orm import declarative_base, sessionmaker
import os
from dotenv import load_dotenv
import csv

# Load environment variables
load_dotenv()

server = os.getenv('AZURE_SQL_SERVER')
database = os.getenv('AZURE_SQL_DATABASE')
username = urllib.parse.quote_plus(os.getenv('AZURE_SQL_USER'))
password = urllib.parse.quote_plus(os.getenv('AZURE_SQL_PASSWORD'))
port = os.getenv('AZURE_SQL_PORT')

conn_str = f'mssql+pymssql://{username}:{password}@{server}/{database}'

# Create engine and base
engine = create_engine(conn_str)
Base = declarative_base()

# Define the Game model
class Game(Base):
    __tablename__ = 'col_T'
    
    Year = Column(Integer, primary_key=True)
    Albania = Column(Float)
    Algeria = Column(Float)
    Argentina = Column(Float)
    Austria = Column(Float)
    Bahamas = Column(Float)
    Bahrain = Column(Float)
    Bolivia = Column(Float)
    Chile = Column(Float)
    Colombia = Column(Float)
    Czechia = Column(Float)
    Denmark = Column(Float)
    Ecuador = Column(Float)
    Egypt = Column(Float)
    El_Salvador = Column(Float)
    Finland = Column(Float)
    Georgia = Column(Float)
    Iran = Column(Float)
    Iraq = Column(Float)
    Latvia = Column(Float)
    Malaysia = Column(Float)
    Moldova = Column(Float)
    New_Zealand = Column(Float)
    Nigeria = Column(Float)
    Oman = Column(Float)
    Palestine = Column(Float)
    Peru = Column(Float)
    Portugal = Column(Float)
    United_States = Column(Float)

Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Read data from CSV and insert into database
with open('transpose cost of living.csv', 'r') as inFile:
    reader = csv.reader(inFile)
    next(reader)  # Skip header if there's one
        # Convert data types as necessary
    Games =[Game(
    Year=row[0],
    Albania=row[1],
    Algeria=row[2],
    Argentina=row[3],
    Austria=row[4],
    Bahamas=row[5],
    Bahrain=row[6],
    Bolivia=row[7],
    Chile=row[8],
    Colombia=row[9],
    Czechia=row[10],
    Denmark=row[11],
    Ecuador=row[12],
    Egypt=row[13],
    El_Salvador=row[14],
    Finland=row[15],
    Georgia=row[16],
    Iran=row[17],
    Iraq=row[18],
    Latvia=row[19],
    Malaysia=row[20],
    Moldova=row[21],
    New_Zealand=row[22],
    Nigeria=row[23],
    Oman=row[24],
    Palestine=row[25],
    Peru=row[26],
    Portugal=row[27],
    United_States=row[28]
) for row in reader]
    session.add_all(Games)

# Commit the session to save the data to the database
session.commit()

# Close the session
session.close()