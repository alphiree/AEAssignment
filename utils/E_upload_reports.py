## Importing Configuration Details
from config.config import bucket_name,reports_folder,folder_alias

## Importing dependencies
import boto3
import datetime

## Importing dictionary from reports
from utils.D2_reports import queries_dict

## Setting TODAY variable as date today
TODAY = datetime.datetime.now().strftime("%Y-%m-%d")



def upload_reports():
    """
    Upload reports to S3 bucket
    """
    print('')
    try:
        s3 = boto3.resource("s3")
        bucket = s3.Bucket(bucket_name)
        for team_report in  queries_dict.keys():
            print(f"Uploading {team_report} Report to S3...")
            bucket.upload_file(
                Key=f"{reports_folder}/{folder_alias}/{team_report}_report_{TODAY}.csv",
                Filename=f"{reports_folder}/{team_report}.csv"
            )
            print(f'Done! Saved as {reports_folder}/{folder_alias}/{team_report}_report_{TODAY}.csv')

        ## Print Success
        print("Reports Upload Successful!")
    except Exception as e:
        ## Print Error
        print(f"Reports Upload Error: {e}")