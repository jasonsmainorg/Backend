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
    __tablename__ = 'Histogram'
    
    Idx = Column(Integer, primary_key=True)
    Min_Price = Column(Float)
    app_ID = Column(Float)


Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Read data from CSV and insert into database
with open('min_price.csv', 'r') as inFile:
    reader = csv.reader(inFile)
    next(reader)  # Skip header if there's one
        # Convert data types as necessary
    Games =[Game(
    Idx=row[0],
    Min_Price=row[1],
    app_ID=row[2],
) for row in reader]
    session.add_all(Games)

# Commit the session to save the data to the database
session.commit()

# Close the session
session.close()