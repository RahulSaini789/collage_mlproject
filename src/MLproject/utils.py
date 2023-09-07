import os
import pymysql
import sys
import pandas as pd
from dotenv import load_dotenv
from src.MLproject.logger import logging
from src.MLproject.exception import CustomException




load_dotenv()


host=os.getenv("host")
user=os.getenv("user")
password=os.getenv("password")
db=os.getenv("db")

def read_sql_data():
    logging.info("reading SQL database Data...")
    try:
        mydb = pymysql.connect(
            host=host,
            user=user,
            password=password,
            db=db
        )
        logging.info("Connection Established", mydb)
        df=pd.read_sql_query('Select * from StudentsPerformance',mydb)
        print(df.head())

        return df


    except Exception as ex:
        raise CustomException(ex)