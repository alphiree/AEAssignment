## Changing the folder_alias to my last name and initials
folder_alias = "LUPAGUE_RMJM"

##=====================================##
## S3 Bucket Details
bucket_name = "test-ae-exam-public-lupague"
bucket_data_path = "data"
bucket_report_path = "reports"
access_key_id = "AKIAZUQXITMDOQDBJMMJ"
secret_access_key = "2QPw6jLyW8oqqj81dsnHY4Ggg7ElPZZqWa8CNaH"

##=====================================##
## Database Details
environment = "prod"
# host = "company1@country.co"
# database = "platform_prod"
# user = "analytics"
# password = "securepassword"

## Testing purposes
host = "localhost"
database = "postgres"
user = "postgres"
#or
# user = os.environ['postgres_user']
password = "Postgre2201"
#or
# password = os.environ['postgres_pass']

## Table name
table_name = "events"
##=====================================##
## Folder Details
reports_folder = "reports"
data_folder = "data"
##=====================================##
## Datatypes of the table
datatypes = {
    "transaction_id": "INT",
    "purchase_price": "FLOAT",
    "product_value": "FLOAT",
    "product_name": "VARCHAR(255)",
    "first_name": "VARCHAR(255)",
    "last_name": "VARCHAR(255)",
    "email": "VARCHAR(255)",
    "gender": "VARCHAR(255)",
    "customer_country": "VARCHAR(255)",
    "client_country": "VARCHAR(255)",
}
