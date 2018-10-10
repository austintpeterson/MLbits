#Austin Peterson
#used to convert csv data to standardized sql db

import json
import sqlite3
import time
import os
from pathlib import Path



def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

def execute_sql_comm(conn, sql_comm):
    try:
        c = conn.cursor()
        c.execute(sql_comm)
    except Error as e:
        print(e)

def main():
    database = "thesis.db"
    mypath = Path().absolute()
    print(mypath)

