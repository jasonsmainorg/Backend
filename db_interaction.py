import urllib.parse
from sqlalchemy import create_engine, Column, Integer, String, Float, BigInteger, Date
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

    def __init__(self, appid: int, name: str, developer: str, publisher: str, 
                 score_rank: int = None, positive: int = None, negative: int = None, 
                 userscore: float = None, owners: str = None, average_forever: int = None, 
                 average_2weeks: int = None, median_forever: int = None, 
                 median_2weeks: int = None, price: float = None, initialprice: float = None, 
                 discount: int = None, ccu: int = None):
        self.appid = appid
        self.name = name
        self.developer = developer
        self.publisher = publisher
        self.score_rank = score_rank
        self.positive = positive
        self.negative = negative
        self.userscore = userscore
        self.owners = owners
        self.average_forever = average_forever
        self.average_2weeks = average_2weeks
        self.median_forever = median_forever
        self.median_2weeks = median_2weeks
        self.price = price
        self.initialprice = initialprice
        self.discount = discount
        self.ccu = ccu

# Define the Survey model
class Survey(Base):
    __tablename__ = 'SteamHWSurveys'
    
    date = Column(Float, primary_key=True)
    category = Column(String(255))
    name = Column(String(255))
    change = Column(Float, nullable=True)
    percentage = Column(Float, nullable=True)

    def __init__(self, date: float, category: str, name: str, change: float, percentage: float):
        self.date = date
        self.category = category
        self.name = name
        self.change = change
        self.percentage = percentage

Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Read data from CSV and insert into database
with open('output.csv', 'r') as inFile:
    reader = csv.reader(inFile)
    next(reader)  # Skip header if there's one
        # Convert data types as necessary
    Games =[Game(
        appid=int(row[0]),
        name=row[1],
        developer=row[2],
        publisher=row[3],
        score_rank=int(row[4]) if row[4] else None,
        positive=int(row[5]),
        negative=int(row[6]),
        userscore=float(row[7]) if row[7] else None,
        owners=row[8],
        average_forever=int(row[9]) if row[9] else None,
        average_2weeks=int(row[10]) if row[10] else None,
        median_forever=int(row[11]) if row[11] else None,
        median_2weeks=int(row[12]) if row[12] else None,
        price=float(row[13])/100 if row[13] else None,
        initialprice=float(row[14])/100 if row[14] else None,
        discount=int(row[15]) if row[15] else None,
        ccu=int(row[16]) if row[16] else None
    ) for row in reader]
    session.add_all(Games)


    Surveys =[Survey(
        date=float(row[0]),
        category=row[1],
        name=row[2],
        change=float(row[3]),
        percentage=float(row[4]) if row[4] else None,
    ) for row in reader]
    session.add_all(Surveys)


# Commit the session to save the data to the database
session.commit()

# Close the session
session.close()