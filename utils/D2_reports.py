## Importing Configuration Details
from config.config import host, database, user, password, table_name,reports_folder

## Importing dependencies
import pandas as pd
from sqlalchemy import create_engine,text
import os

## Importing all the queries
from utils.D1_sql_queries import *

## Creating dictionary for list of quries:
queries_dict = {
    "finance":FINANCE_QUERY,
    "marketing":MARKETING_QUERY,
}

## Creating Reports
def create_reports():
    '''
    Create reports from the PostgreSQL database and turns it into csv file.
    '''
    print('')
    try:
        connection_string = f"postgresql://{user}:{password}@{host}/{database}"
        engine = create_engine(connection_string)  
        
        ## Creating reports folder if it not exists yet.
        if not os.path.exists(reports_folder):
            os.makedirs(reports_folder)


        for team_report in  queries_dict.keys():

            print(f"Creating and Saving {team_report} Report...")
            df_report = pd.DataFrame(engine.connect().execute(text(queries_dict[team_report])))

            df_report.to_csv(f"{reports_folder}/{team_report}.csv")
            print(f'Done! Saved at {reports_folder}/{team_report}.csv')
        
        engine.dispose()

    except Exception as e:
        ## Print Error
        print(f"Report Creation Error: {e}")    