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
    __tablename__ = 'steamhwsv'
    
    appid = Column(Integer, primary_key=True)
    game_name = Column(String(255))
    minimum_requirement_pc = Column(Text)
    minimum_requirement_mac = Column(Text)
    minimum_requirement_linux = Column(Text)
    recommended_requirement_pc = Column(Text)
    recommended_requirement_mac = Column(Text)
    recommended_requirement_linux = Column(Text)
    Albania_price = Column(Float)
    Algeria_price = Column(Float)
    Argentina_price = Column(Float)
    Austria_price = Column(Float)
    Bahamas_price = Column(Float)
    Bahrain_price = Column(Float)
    Bolivia_price = Column(Float)
    Chile_price = Column(Float)
    Colombia_price = Column(Float)
    Czechia_price = Column(Float)
    Denmark_price = Column(Float)
    Ecuador_price = Column(Float)
    Egypt_price = Column(Float)
    El_Salvador_price = Column(Float)
    Finland_price = Column(Float)
    Georgia_price = Column(Float)
    Iran_price = Column(Float)
    Iraq_price = Column(Float)
    Latvia_price = Column(Float)
    Malaysia_price = Column(Float)
    Moldova_price = Column(Float)
    New_Zealand_price = Column(Float)
    Nigeria_price = Column(Float)
    Oman_price = Column(Float)
    Palestine_price = Column(Float)
    Peru_price = Column(Float)
    Portugal_price = Column(Float)
    US_price = Column(Float)

Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Read data from CSV and insert into database
with open('region_price.csv', 'r') as inFile:
    reader = csv.reader(inFile)
    next(reader)  # Skip header if there's one
        # Convert data types as necessary
    Games =[Game(
    appid=row[0],
    game_name=row[1],
    minimum_requirement_pc=row[2],
    minimum_requirement_mac=row[3],
    minimum_requirement_linux=row[4],
    recommended_requirement_pc=row[5],
    recommended_requirement_mac=row[6],
    recommended_requirement_linux=row[7],
    Albania_price=row[8],
    Algeria_price=row[9],
    Argentina_price=row[10],
    Austria_price=row[11],
    Bahamas_price=row[12],
    Bahrain_price=row[13],
    Bolivia_price=row[14],
    Chile_price=row[15],
    Colombia_price=row[16],
    Czechia_price=row[17],
    Denmark_price=row[18],
    Ecuador_price=row[19],
    Egypt_price=row[20],
    El_Salvador_price=row[21],
    Finland_price=row[22],
    Georgia_price=row[23],
    Iran_price=row[24],
    Iraq_price=row[25],
    Latvia_price=row[26],
    Malaysia_price=row[27],
    Moldova_price=row[28],
    New_Zealand_price=row[29],
    Nigeria_price=row[30],
    Oman_price=row[31],
    Palestine_price=row[32],
    Peru_price=row[33],
    Portugal_price=row[34],
    US_price=row[35]
) for row in reader]
    session.add_all(Games)

# Commit the session to save the data to the database
session.commit()

# Close the session
session.close()