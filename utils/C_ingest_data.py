## Importing Configuration Details
from config.config import host,database,user,password,table_name

## Importing dependencies
import pandas as pd
from sqlalchemy import create_engine


def ingest_data(data):
    '''
    Ingests data into a PostgreSQL database
    '''
    print('')
    try:
        connection_string = f"postgresql://{user}:{password}@{host}/{database}"
        engine = create_engine(connection_string)  

        rows_imported = 0
        print(f'Importing rows {rows_imported} to {len(data)}')
        print(f'Importing the dataframe to {database} database and naming it as "{table_name}" table...')
        ## Saving dataframe to postgres
        data.to_sql(table_name, engine, if_exists="append", index=False)
        rows_imported += len(data)
        print('Data Ingest Successful')

        engine.dispose()
        
    except Exception as e:
        ## Print Error
        print(f"Data Ingestion Error: {e}")     


