## Importing Configuration Details
from config.config import data_folder, reports_folder, folder_alias
## Importing functions from utils folder in order
from utils.A_getting_data import get_daily_data
from utils.B_transform import transform_data
from utils.C_ingest_data import ingest_data
from utils.D2_reports import create_reports
from utils.E_upload_reports import upload_reports

## Importing dependencies
from os import getcwd

## Initializing variables
## Getting the current working directory
working_dir = getcwd()
## S3 File Extraction Path
s3_file_path = f"{data_folder}/platform_transactions.csv"
## File path in working directory
extracted_file_path = f"{working_dir}/platform_transactions.csv"

if __name__ == "__main__":

    ## Getting the data from S3 Bucket.
    get_daily_data(
        download_from=s3_file_path,
        download_to=extracted_file_path,
    )
    ## Clean and Transform the data
    transformed_data = transform_data(extracted_file_path)

    ## Ingest into data lake
    ingest_data(transformed_data)

    ## Creating Reports
    create_reports()

    ## Uploading Reports to the S3 Bucket
    upload_reports()

