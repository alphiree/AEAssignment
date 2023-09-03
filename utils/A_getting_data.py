## Importing Configuration Details
from config.config import bucket_name

## Importing dependencies
import boto3

def get_daily_data(download_from, download_to):
    """
    Get daily data from S3 bucket
    """
    print('')
    try:
        ## Initializing Bucket Resource
        s3 = boto3.resource("s3")
        bucket = s3.Bucket(bucket_name)
        print(f"Extracting {download_from} in {bucket_name} bucket...")
        ## Downloading data from the S3 Bucket:
        bucket.download_file(
            Key = download_from, 
            Filename = download_to,
            )
        ## Print Success
        print("Data Extraction Successful!")
    except Exception as e:
        ## Print Error
        print(f" Data Extraction Error: {e}")





